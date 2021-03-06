import unittest
from test_unittest import TestTeamcityMessages
from test_copy import TestTeamcityCopy

def suite():
    suite = unittest.TestSuite()
    suite.addTest (TestTeamcityMessages())
    suite.addTest (TestTeamcityCopy())

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)
  