import ast
import re
from setuptools import setup
import sys

assert sys.version_info >= (3, 7, 0)
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent


def get_version() -> str:
    package = CURRENT_DIR / "buildbot_reporter" / "__init__.py"
    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
    with open(package, "r", encoding="utf8") as f:
        match = _version_re.search(f.read())
        version = match.group("version") if match is not None else '"unknown"'
    return str(ast.literal_eval(version))


setup(
    name="buildbot_reporter",
    version=get_version(),
    description="Tool to produce buildbot reports",
    keywords="buildbot report test integration",
    author="Pablo Galindo",
    author_email="pablogsal@gmail.com",
    license="MIT",
    packages=["buildbot_reporter"],
    python_requires=">=3.7",
    zip_safe=False,
    install_requires=["aiohttp", "pyperclip", "click"],
    entry_points={
        "console_scripts": [
            "buildbotreporter = buildbot_reporter.__main__:cli"
        ]
    },
)
