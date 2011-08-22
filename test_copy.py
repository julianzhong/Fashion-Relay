#from teamcity.unittestpy import TeamcityTestRunner
import unittest

# COPY = sample of using teamcity
class TestTeamcityCopy(unittest.TestCase):

  def testPassCopy(self):
    self.assertEqual(1, 1, 'Error: testPass')

  def testAssertEqualCopy(self):
    self.assertEqual(1, 2, 'Error: testAssertEqual')

  def testAssertEqualMsgCopy(self):
    self.assertEqual("1", "3", 'Error: testAssertEqualMsg')

if __name__ == '__main__':
  unittest.main()
  #unittest.main(testRunner=TeamcityTestRunner())
