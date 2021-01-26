import unittest

from testcases.first_unit_test import FirstUnitTest
from testcases.second_unit_test import SecondUnitTest

class TestSuite(unittest.TestSuite):
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(FirstUnitTest("FirstUnitTest"))
        suite.addTest(SecondUnitTest("SecondUnitTest"))
        return suite

if __name__ == "__main__":
    unittest.main()
