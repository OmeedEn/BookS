import unittest

import RandomQueue


class TestRandomQueue(unittest.TestCase):

    def test_remove(self):
        rand = RandomQueue.RandomQueue()
        rand.add(1)
        rand.add(2)
        rand.add(3)
        rand.add(4)
        rand.add(5)
        rand.remove()
        rand.remove()
        rand.remove()
        rand.remove()
        print(rand)


if __name__ == '__main__':
    unittest.main()
