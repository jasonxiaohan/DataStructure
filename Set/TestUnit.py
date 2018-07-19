import unittest
from DataStructure.Set.BSTSet import BSTSet


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bst = BSTSet()
        self.bst.add(1)
        self.bst.add(1)
        self.bst.add(2)
        self.bst.add(5)

    def test_something(self):
        self.assertEqual(True, True)

    """
    测试集合中的getSize()方法
    """
    def test_setAdd(self):
        self.assertEqual(self.bst.getSize(), 3)

    def test_setContains(self):
        self.assertEqual(self.bst.contains(5), True)

if __name__ == '__main__':
    unittest.main()
