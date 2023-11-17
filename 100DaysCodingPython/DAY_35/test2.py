'''testing module'''


import unittest

from main import Caculator, do_something, to_lower, to_upper


class my_test(unittest.TestCase):
    '''test do_something function'''
    '''it isn't an accident that all the methods' names start with the word test. '''

    def test_do_something(self):  #
        self.assertEqual(do_something(3), 4)

    def test_to_upper(self):
        params = "samuel"
        '''params'''
        self.assertEqual(to_upper(params), "SAMUEL", "Not the same")

    def test_to_lower(self):
        params = "samuel"
        self.assertEqual(to_lower(params),
                         "samuel", "they are not equal ")

    def setUp(self):
        self.caculator = Caculator(20, 10)

    def test_Caculator1(self):
        caculator = Caculator(8, 2)
        self.assertEqual(caculator.get_sum(), 10, "'The sum is wrong.")

    def test_Caculator2(self):
        caculator = Caculator(8, 2)
        self.assertEqual(caculator.get_diffrence(), 6, "The diff is wrong")


if __name__ == '__main__':
    unittest.main()
