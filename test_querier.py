import unittest
import querier



class Test(unittest.TestCase):
    def test_database_connection(self):

        self.assertEqual(str(type(querier.con)), "<class 'sqlite3.Connection'>")

    def test_database_cursor(self):

        self.assertEqual(str(type(querier.cur)), "<class 'sqlite3.Cursor'>")


