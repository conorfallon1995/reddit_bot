from unittest import TestCase


class Test(TestCase):
    def test_string_query(self):
        self.assertNotEqual(self.return_string, "")
