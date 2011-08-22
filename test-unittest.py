from teamcity.unittestpy import TeamcityTestRunner
import unittest

class TestTeamcityMessages(unittest.TestCase):

  def testPass(self):
    self.assertEqual(1, 1, 'Error: testPass')

  def testAssertEqual(self):
    self.assertEqual(1, 2, 'Error: testAssertEqual')

  def testAssertEqualMsg(self):
    self.assertEqual("1", "3", 'Error: testAssertEqualMsg')

  def testAssert(self):
    self.assertTrue(False)

  def testFail(self):
    self.fail("SET it fail")

  def testException(self):
    raise Exception("some exception")

if __name__ == '__main__':
  unittest.main(testRunner=TeamcityTestRunner())
