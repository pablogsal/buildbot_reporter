import asyncio
from datetime import datetime
import sys

import aiohttp
import re
import os

import click
from dateparser import parse
import pyperclip

from .buildbotapi import BuildBotAPI

DESCRIPTION_REPORT = """\
Produce buildbot failure reports from buildbot build urls.
"""

DESCRIPTION_LAST_FAILURES = """\
Obtain urls for last failures.
"""

BUILDBOT_URL_REGEXP = re.compile(
    r"https://buildbot.python.org/all/#/?builders/"
    r"(?P<builder>\d+)/builds/(?P<build>\d+)"
)

TEMPLATE = """\
BUILDBOT FAILURE REPORT
=======================

Builder name: {buildername}
Builder url: https://buildbot.python.org/all/#/builders/{builderid}/
Build url: https://buildbot.python.org/all/#/builders/{builderid}/builds/{buildid}

Failed tests
------------

{failed_tests_text}

Test leaking resources
----------------------

{leak_tests_text}

Build summary
-------------

{build_summary_text}

Tracebacks
----------

```traceback
{tracebacks_texts}
```

Current builder status
----------------------

{current_builder_status_text}

Commits
-------

{commits_text}

Other builds with similar failures
----------------------------------

{other_builds_text}
"""


async def main_report(builder, build, token, copy, raw_log):
    async with aiohttp.ClientSession() as session:
        api = BuildBotAPI(session)
        await api.authenticate(token=token)
        this_failure = await api.get_build(builder, build)

        if raw_log:
            report = this_failure.logs.raw_logs
        else:
            recent_failures = list(await api.get_recent_failures())
            other_failures = [
                failure for failure in recent_failures if this_failure != failure
            ]

            logs = this_failure.logs

            other_failed_builds = [
                failure
                for failure in other_failures
                if set(logs.get_failed_subtests())
                & set(failure.logs.get_failed_subtests())
                or set(logs.get_leaks()) & set(failure.logs.get_leaks())
            ]

            other_builds_text = "\n".join(
                f"-  https://buildbot.python.org/all/#/builders/{build.builder.id}/builds/{build.id}"
                for build in other_failed_builds
            )

            failed = "\n".join(
                f"- {test.parent} ({test.name})\n"
                for test in logs.get_failed_subtests()
            )
            leaks = "\n".join(
                f"- {test.name} is leaking {test.resource}\n"
                for test in logs.get_leaks()
            )
            tracebacks = "\n\n".join(traceback for traceback in logs.get_tracebacks())

            if await api.is_builder_failing_currently(this_failure.builder):
                current_builder_status_text = "The builder is failing currently"
            else:
                current_builder_status_text = (
                    "Last builds for the builder are successful. This error might be "
                    "already fixed or it may be a race condition."
                )

            commits = "\n".join(f"- {commit.sha}\n" for commit in this_failure.changes)

            common_commits = {commit.sha for commit in this_failure.changes}
            for build in other_failed_builds:
                common_commits = common_commits & {change.sha for change in build.changes}

            if common_commits:
                extra_text = "\n".join(f"- {sha}" for sha in common_commits)
                other_builds_text += f"\n\nCommon commits for all builds:\n\n{extra_text}"

            report = TEMPLATE.format(
                buildername=this_failure.builder.name,
                builderid=this_failure.builder.id,
                buildid=this_failure.id,
                failed_tests_text=failed,
                leak_tests_text=leaks,
                build_summary_text=logs.test_summary(),
                tracebacks_texts=tracebacks,
                current_builder_status_text=current_builder_status_text,
                other_builds_text=other_builds_text,
                commits_text=commits,
            )

    if copy:
        pyperclip.copy(report)
        print("Report copied to clipboard!")
    else:
        print(report)


async def main_last_failures(since, limit, token):
    async with aiohttp.ClientSession() as session:
        api = BuildBotAPI(session)
        await api.authenticate(token=token)
        last_failures = await api.get_recent_failures(limit=limit)
        if since is not None:
            last_failures = [failure for failure in last_failures if
                             datetime.utcfromtimestamp(failure.complete_at) > since]
        for build in last_failures:
            print(f"-  https://buildbot.python.org/all/#/builders/{build.builder.id}/builds/{build.id}")


@click.group()
@click.option(
    "--token",
    type=str,
    help="GitHub personal token to authenticate with the buildbot API",
)
@click.pass_context
def cli(ctx, token):
    if ctx.obj is None:
        ctx.obj = {}
    if token is None:
        token = os.getenv("GH_AUTH")
    if token is None:
        print(
            "A GitHub token must be specified with --token or in the GH_AUTH env variable",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(1)
    ctx.obj['TOKEN'] = token


@cli.command(help=DESCRIPTION_LAST_FAILURES)
@click.option("--since", type=str)
@click.option("--limit", type=int, default=100)
@click.pass_context
def last_failures(ctx, since, limit):
    loop = asyncio.get_event_loop()
    token = ctx.obj['TOKEN']
    if since is not None:
        since = parse(since)
    loop.run_until_complete(main_last_failures(since, limit, token))


@cli.command(help=DESCRIPTION_REPORT)
@click.argument("url", type=str, required=True)
@click.option(
    "--copy/--no-copy", default=False, help="Copy the report to the clipboard"
)
@click.option("--raw-log", is_flag=True, help="Show only the raw log for the build")
@click.pass_context
def report(ctx, url, *args, **kwargs):
    match = BUILDBOT_URL_REGEXP.match(url)
    if not match:
        print(
            "The url is not recognized as a Python buildbot url",
            file=sys.stderr,
            flush=True,
        )
        return
    builder, build = match.groups()
    loop = asyncio.get_event_loop()
    token = ctx.obj['TOKEN']
    loop.run_until_complete(main_report(builder, build, token, *args, **kwargs))



if __name__ == "__main__":
    cli(obj={})
