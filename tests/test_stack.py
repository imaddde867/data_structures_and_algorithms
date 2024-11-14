import sys
print("sys.path:", sys.path)
sys.path.insert(0, r"C:\Users\vladt\OneDrive - O365 Turun yliopisto\Desktop\project_root")

import unittest
from data_structures.stack import Stack
from custom_object import CustomObject

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.peek(), 10)

    def test_pop(self):
        self.stack.push(20)
        item = self.stack.pop()
        self.assertEqual(item, 20)
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        self.stack.push(30)
        self.stack.push(40)
        self.assertEqual(self.stack.peek(), 40)
        self.assertEqual(self.stack.size(), 2)

    def test_size(self):
        self.stack.push(50)
        self.stack.push(60)
        self.assertEqual(self.stack.size(), 2)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_with_integers(self):
        numbers = [1, 2, 3, 4, 5]
        for num in numbers:
            self.stack.push(num)
        for num in reversed(numbers):
            self.assertEqual(self.stack.pop(), num)
        self.assertTrue(self.stack.is_empty())

    def test_with_strings(self):
        words = ["apple", "banana", "cherry"]
        for word in words:
            self.stack.push(word)
        for word in reversed(words):
            self.assertEqual(self.stack.pop(), word)
        self.assertTrue(self.stack.is_empty())

    def test_with_custom_objects(self):
        objects = [CustomObject(i) for i in range(5)]
        for obj in objects:
            self.stack.push(obj)
        for obj in reversed(objects):
            self.assertEqual(self.stack.pop(), obj)
        self.assertTrue(self.stack.is_empty())

if __name__ == '__main__':
    unittest.main()
