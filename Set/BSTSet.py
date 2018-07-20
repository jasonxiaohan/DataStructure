# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 15:32
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : BSTSet.py
# @Software: PyCharm

from DataStructure.BST.BinarySearchTree import BinarySearchTree
from DataStructure.Set.Set import Set

"""
集合实现类
"""
class BSTSet(Set):
    bst = None
    def __init__(self):
        self.bst = BinarySearchTree()

    def add(self, e):
        self.bst.add(e)

    def remove(self, e):
        return self.bst.remove(e)

    def contains(self, e):
        return self.bst.contains(e)

    def getSize(self):
        return self.bst.getSize()

    def isEmpty(self):
        return self.bst.isEmpty()
