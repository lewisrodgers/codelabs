import unittest
from unittest.mock import patch


class TestFoo(unittest.TestCase):
    @patch('foo.FooClass.msg', return_value='hello')
    def test_msg(self, msg):
        self.assertEqual(msg('hello'), 'hello')


if __name__ == '__main__':
    unittest.main()