from teamcity.unittestpy import TeamcityTestRunner
import unittest

# COPY = sample of using teamcity
class TestTeamcityCopy(unittest.TestCase):

  def testPass(self):
    self.assertEqual(1, 1, 'Error: testPass')

  def testAssertEqual(self):
    self.assertEqual(1, 2, 'Error: testAssertEqual')

  def testAssertEqualMsg(self):
    self.assertEqual("1", "3", 'Error: testAssertEqualMsg')

if __name__ == '__main__':
  unittest.main(testRunner=TeamcityTestRunner())
