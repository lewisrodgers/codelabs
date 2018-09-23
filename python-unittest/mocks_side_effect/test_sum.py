import unittest
from unittest.mock import patch

import sum

def mock_sum(a, b):
    # remove `time.sleep` from original function in `sum.py` so we don't have to
    # wait for the delay during the test.
    return a + b

class TestSum(unittest.TestCase):
    @patch('sum.Calculator.sum', side_effect=mock_sum)
    def test_sum_mock(self, sum):
        self.assertEqual(sum(1,2), 3)

    # @patch('sum.Calculator.sum')
    # def test_sum_mock(self, sum):
    #     sum.side_effect = mock_sum
    #     self.assertEqual(sum(1,2), 3)


if __name__ == '__main__':
    unittest.main()