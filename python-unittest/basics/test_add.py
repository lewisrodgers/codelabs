import unittest
from add import add


class FooTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("Print before all tests run")

    @classmethod
    def tearDownClass(self):
        print("Print after all tests run")

    def setUp(self):
        print("Run before each test")

    def tearDown(self):
        print("Run after each test")
    
    def test_add(self):
        sum = add(1, 2)
        self.assertEqual(3, sum)

    def test_add_negative_numbers(self):
        sum = add(-1, -2)
        self.assertEqual(-3, sum)

