import unittest

import addon_utils


addon_utils.enable("sample_addon", default_set=True)

runner = unittest.TextTestRunner()
suite = unittest.TestSuite()
testLoader = unittest.TestLoader()

suite.addTests(testLoader.discover("./tests", "test_npanel.py"))
suite.addTests(testLoader.discover("./tests", "test_nice.py"))


result = runner.run(suite)
if len(result.errors) + len(result.failures) != 0:
    exit(1)
