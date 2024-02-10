import unittest

from main2 import my_sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        param1 = 10
        param2 = 20
        result = my_sum(param1,param2)
        self.assertEqual(result, 30)


if __name__ == "__main__":
    unittest.main()
