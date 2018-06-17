from app import app
import unittest


class TasksTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass
    
    def test_tasks(self):
        result = self.app.get('/todo/api/v1/tasks')
        self.assertEqual(result.status_code, 200)

    def test_not_found(self):
        result = self.app.get('/todo/api/v1/tasks/3')
        self.assertEqual(result.status_code, 404)