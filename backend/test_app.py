import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health(self):
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'status', response.data)
    
    def test_clock(self):
        response = self.app.get('/api/time')
        #self.assertEqual(response.status_code, 200)
        #self.assertIn(b'time', response.data)
        print(response.data)



if __name__ == "__main__":
    unittest.main()