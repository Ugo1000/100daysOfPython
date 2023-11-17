'''This module test the random game '''
from myGame import my_guess
import unittest


class Test_Game(unittest.TestCase):
    def test_correct_guess(self):
        """Correct guess"""
        answer = 5
        guess = 5
        result = my_guess(5, 5, "sam")
        self.assertTrue(result)

    def test_wrong_guess(self):
        '''Wrong guess'''
        answer = 5
        guess = 6
        result = my_guess(6, 5, "sam")
        self.assertFalse(result)

    def test_out_of_range_guess(self):
        '''Out of range guess'''
        answer = 5
        guess = 11
        result = my_guess(11, 5, "sam")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
