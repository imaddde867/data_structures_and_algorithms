import sys
sys.path.insert(0, r"C:\Users\vladt\OneDrive - O365 Turun yliopisto\Desktop\project_root")


import unittest
from data_structures.queue import Queue
from custom_object import CustomObject

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.peek(), 10)

    def test_dequeue(self):
        self.queue.enqueue(20)
        item = self.queue.dequeue()
        self.assertEqual(item, 20)
        self.assertTrue(self.queue.is_empty())

    def test_peek(self):
        self.queue.enqueue(30)
        self.queue.enqueue(40)
        self.assertEqual(self.queue.peek(), 30)
        self.assertEqual(self.queue.size(), 2)

    def test_size(self):
        self.queue.enqueue(50)
        self.queue.enqueue(60)
        self.assertEqual(self.queue.size(), 2)

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_with_integers(self):
        numbers = [1, 2, 3, 4, 5]
        for num in numbers:
            self.queue.enqueue(num)
        for num in numbers:
            self.assertEqual(self.queue.dequeue(), num)
        self.assertTrue(self.queue.is_empty())

    def test_with_strings(self):
        words = ["apple", "banana", "cherry"]
        for word in words:
            self.queue.enqueue(word)
        for word in words:
            self.assertEqual(self.queue.dequeue(), word)
        self.assertTrue(self.queue.is_empty())

    def test_with_custom_objects(self):
        objects = [CustomObject(i) for i in range(5)]
        for obj in objects:
            self.queue.enqueue(obj)
        for obj in objects:
            self.assertEqual(self.queue.dequeue(), obj)
        self.assertTrue(self.queue.is_empty())

if __name__ == '__main__':
    unittest.main()
