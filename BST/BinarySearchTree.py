# -*- coding:utf-8 -*-
"""
@author daixiaohan
二分搜索树
"""

class BinarySearchTree:
    class Node:
        e = None
        left = right = None

        def __init__(self, e):
            self.e = e

    root = None
    size = 0

    def __init__(self):
        self.size = 0

    def geSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, e):
        """
        if self.root == None:
            self.root = self.Node(e)
            self.size += 1
        else:
            self.__add(self.root, e)
        """
        root = self.__add(e)
    """
   向node为根的二分搜索树中插入元素e，递归算法 
   返回插入新节点后二分搜索树的根
    """
    def __add(self, node, e):
        """
        if node.e == e:
            return
        else:
            if e < node.e and node.left == None:
                node.left = self.Node(e)
                self.size += 1
                return
            elif e > node.e and node.right == None:
                node.right = self.Node(e)
                self.size += 1
                return
        """
        if node == None:
            self.size += 1
            return self.Node(e)
        if e < node.e:
            node.left = self.__add(node.left, e)
        elif e> node.e:
            node.right = self.__add(node.right, e)
        return node