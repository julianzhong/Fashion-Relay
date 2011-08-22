import unittest
from test_unittest import TestTeamcityMessages

def suite():

    suite = unittest.TestSuite()

    suite.addTest (TestTeamcityMessages())

    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run (test_suite)
  