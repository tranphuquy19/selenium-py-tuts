import unittest

from tests.google.first_unit_test import FirstUnitTest
from tests.google.second_unit_test import SecondUnitTest

class TestSuite(unittest.TestSuite):
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(FirstUnitTest("FirstUnitTest"))
        suite.addTest(SecondUnitTest("SecondUnitTest"))
        return suite

if __name__ == "__main__":
    unittest.main(verbosity=2)
