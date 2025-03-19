from main import *
import unittest

class TestMyMethods(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(Add(""), 0)

    def test_add_one_num(self):
        self.assertEqual(Add("1"), 1)

    def test_add_two_num(self):
        self.assertEqual(Add("1,3"), 4)

    def test_multi(self):
        self.assertEqual(Add("1,3,3"), 7)

    def test_next_line(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_next_line1(self):
        self.assertEqual(Add("\n2,3"), -1)

    def test_next_line2(self):
        self.assertEqual(Add("1,\n"), -1)

    def test_next_line3(self):
        self.assertEqual(Add("\n,3"), -1)
