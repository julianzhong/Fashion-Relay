#from teamcity.unittestpy import TeamcityTestRunner
import unittest

# sample of using teamcity
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
    self.fail("Always fail")

  def testException(self):
    raise Exception("some exception")

if __name__ == '__main__':
  unittest.main()
  #unittest.main(testRunner=TeamcityTestRunner())
