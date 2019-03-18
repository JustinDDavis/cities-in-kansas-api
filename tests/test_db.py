
import unittest
from db.db import Database

class TestDatabase(unittest.TestCase):
    def test_initialization(self):
        db = Database()
        default_db_name = 'city_names.txt'

        self.assertEqual(db.file_name, default_db_name, 'should have the same default database file')
        self.assertEqual(db.data, [], 'should contain an empty list')
    
    def test_parse_db_file(self):
        """ Check the test file, and make sure our validation works correctly """
        db = Database()
        db.connect()
        self.assertTrue(db.contains(['Wichita', 'St. Paul', 'Fort Riley-Camp Whiteside'])) 
        self.assertFalse(db.contains(['W!ch!ta', 'St`Paul', 'F0rt R!Ley']))
