import unittest

from DataStructure.Set.LinkedListSet import LinkedListSet
class LinkedListSetTest(unittest.TestCase):
    def setUp(self):
        self.set = LinkedListSet()
        self.set.add(1)
        self.set.add(1)
        self.set.add(2)
        self.set.add(3)

    def test_getSize(self):
        self.set.remove(2)
        self.assertEqual(self.set.getSize(),2)

    def test_isEmpty(self):
        self.assertEqual(self.set.isEmpty(), False)

if __name__ == '__main__':
    unittest.main()
