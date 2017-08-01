import unittest

def my_function_one(my_input):
    return

def my_funtion_two(my_input):
    return

def my_funtion_three(my_input):
    return

class TestFunctionOne(unittest.TestCase):
    def test_function_one_one(self):
        self.assertTrue(True)
    def test_funtion_one_two(self):
        self.assertFalse(False)
    def test_function_one_three(self):
        self.assertEqual(0, 0)

class TestFunctionTwo(unittest.TestCase):
    def test_function_two_one(self):
        self.assertTrue(True)
    def test_function_two_two(self):
        self.assertFalse(False)
    def test_function_two_three(self):
        self.assertEqual(0,0)

class TestFunctionThree(unittest.TestCase):
    def test_function_three_one(self):
        self.assertTrue(True)
    def test_function_three_two(self):
        self.assertFalse(False)
    def test_function_three_three(self):
        self.assertEqual(0, 0)

unittest.main()
