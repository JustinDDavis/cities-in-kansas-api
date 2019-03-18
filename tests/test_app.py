import unittest

from app.app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """ Get Flask Test client """ 
        self.app = app.test_client()
    
    def test_get_cities(self):
        """ Return all cities """
        response = self.app.get('/api/ks')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Wichita' in response.data)
        self.assertFalse(b'PythonTown' in response.data)
    
    def test_get_filtered_cities(self):
        response = self.app.get('/api/ks?startswith=a')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Arkansas City' in response.data)
        self.assertFalse(b'Wichita' in response.data)