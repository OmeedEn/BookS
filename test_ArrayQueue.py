import unittest
import ArrayQueue


class TestArrayQueue(unittest.TestCase):
    def test_add(self):
        queue = ArrayQueue.ArrayQueue()
        queue.add(1)
        result = queue.size()
        self.assertEqual(result, 1)

    def test_resize(self):
        queue = ArrayQueue.ArrayQueue()
        for i in range(20):
            queue.add(1)

        size = queue.size()
        self.assertNotEqual(size, len(queue.a))
        self.assertLess(size, len(queue.a))

    def test_remove(self):
        queue = ArrayQueue.ArrayQueue()
        queue.add(1)
        queue.remove()
        size = queue.size()
        self.assertEqual(queue.remove(), 0)
        self.assertEqual(size, 0)
        with self.assertRaises(IndexError):
            queue.remove()

    def test_remove_order(self):
        queue = ArrayQueue.ArrayQueue()
        queue.add(3)
        queue.add(2)
        queue.add(3)
        queue.add(4)
        queue.add(5)
        print(queue)





if __name__ == '__main__':
    unittest.main()
