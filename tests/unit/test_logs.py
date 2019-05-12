from buildbot_reporter.logparser import Logs


class TestSubTestParsing:
    def test_subtest_capture(self):
        # GIVEN
        raw_logs = """\
test_with_two_items (test.test_tools.test_unparse.UnparseTestCase) ... ok
======================================================================
FAIL: test_files (test.test_tools.test_unparse.DirectoryTestCase) (filename='/root/buildarea/3.x.angelico-debian-amd64/build/Lib/test/test_typing.py')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/root/buildarea/3.x.angelico-debian-amd64/build/Lib/test/test_tools/test_unparse.py", line 309, in test_files
    self.check_roundtrip(source)
  File "/root/buildarea/3.x.angelico-debian-amd64/build/Lib/test/test_tools/test_unparse.py", line 132, in check_roundtrip
    self.assertASTEqual(ast1, ast2)
  File "/root/buildarea/3.x.angelico-debian-amd64/build/Lib/test/test_tools/test_unparse.py", line 124, in assertASTEqual
    self.assertEqual(ast.dump(ast1), ast.dump(ast2))
AssertionError: 'Modu[88178 chars]kind=\'u\')], ctx=Load())), ctx=Load()))], dec[421987 chars]=[])' != 'Modu[88178 chars]kind=None)], ctx=Load())), ctx=Load()))], deco[421986 chars]=[])'

----------------------------------------------------------------------
test_with_as (test.test_tools.test_unparse.UnparseTestCase) ... ok
"""
        # WHEN

        failed_subtests = list(Logs(raw_logs).get_failed_subtests())

        # THEN

        assert len(failed_subtests) == 1
        test = failed_subtests[0]
        assert test.parent == "test_files"
        assert test.name == "test.test_tools.test_unparse.DirectoryTestCase"

    def test_subtest_capture_no_filepath(self):
        # GIVEN
        raw_logs = """\
test_with_two_items (test.test_tools.test_unparse.UnparseTestCase) ... ok
======================================================================
FAIL: test_files (test.test_tools.test_unparse.DirectoryTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/root/buildarea/3.x.angelico-debian-amd64/build/Lib/test/test_tools/test_unparse.py", line 309, in test_files
    self.check_roundtrip(source)
  File "/root/buildarea/3.x.angelico-debian-amd64/build/Lib/test/test_tools/test_unparse.py", line 132, in check_roundtrip
    self.assertASTEqual(ast1, ast2)
  File "/root/buildarea/3.x.angelico-debian-amd64/build/Lib/test/test_tools/test_unparse.py", line 124, in assertASTEqual
    self.assertEqual(ast.dump(ast1), ast.dump(ast2))
AssertionError: 'Modu[88178 chars]kind=\'u\')], ctx=Load())), ctx=Load()))], dec[421987 chars]=[])' != 'Modu[88178 chars]kind=None)], ctx=Load())), ctx=Load()))], deco[421986 chars]=[])'

----------------------------------------------------------------------
test_with_as (test.test_tools.test_unparse.UnparseTestCase) ... ok
"""
        # WHEN

        failed_subtests = list(Logs(raw_logs).get_failed_subtests())

        # THEN

        assert len(failed_subtests) == 1
        test = failed_subtests[0]
        assert test.parent == "test_files"
        assert test.name == "test.test_tools.test_unparse.DirectoryTestCase"
