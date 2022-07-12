import unittest

import ArrayList


class TestArrayList(unittest.TestCase):
    def test_add(self):
        alist = ArrayList.ArrayList()
        alist.add(0, 1)
        alist.add(1, 2)
        result = alist.size()
        print(alist)
        self.assertEqual(result, 2)

    def test_resize(self):
        alist = ArrayList.ArrayList()
        for i in range(20):
            alist.add(0, 1)

        size = alist.size()
        self.assertNotEqual(size, len(alist.a))
        self.assertLess(size, len(alist.a))

    def test_remove(self):
        alist = ArrayList.ArrayList()
        alist.add(0, 1)
        alist.remove(0)
        size = alist.size()
        self.assertEqual(alist.remove(0), 0)
        self.assertEqual(size, 0)
        with self.assertRaises(IndexError):
            alist.remove(0)

    def test_remove_order(self):
        alist = ArrayList.ArrayList()
        alist.add(0,4)
        alist.add(1,1)
        alist.add(2,3)
        alist.add(3,2)
        alist.add(4,5)
        print(alist)
        value1 = alist.remove(2)
        print(alist)
        value2 = alist.remove(2)
        print(alist)

if __name__ == '__main__':
    unittest.main()
