from unittest import TestCase
from testfixtures import TempDirectory

from src.app.url_shortening import assign_word_to_url


class WebAppFunctionsTestCase(TestCase):
    """
    Test class for web application test cases.
    """
    def test_assign_a_word_to_url(self):
        """Test something"""
        self.assertEquals(assign_word_to_url('http://test'), 'aa')
