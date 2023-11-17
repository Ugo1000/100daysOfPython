# this dont run in production
# unittest

import unittest
import main


# class Testmain(unittest.TestCase):
#     def test_add(self):
#         result = main.add(10, 5)
#         self.assertEqual(result, 15)

    # def test_do_stuff(self):
    #     test_param = 10
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 15)

    # def test_do_stuff2(self):
    #     test_param = "nothing"
    #     result = main.do_stuff(test_param)
    #     self.assertTrue(result, "   ")

    # def test_do_stuff3(self):
    #     test_param = "DO_NOTHING"
    #     result = main.do_stuff(test_param)
    #     self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()
