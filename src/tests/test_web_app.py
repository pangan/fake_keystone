from unittest import TestCase
from testfixtures import TempDirectory


class WebAppFunctionsTestCase(TestCase):
    """
    Test class for web application test cases.
    """
    def test_something(self):
        """Test something"""
        self.assertEqual(1,1)