#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: RBTree.py
@time: 2018/8/14 23:20
@desc:
"""
from DataStructure.FileOperation import FileOperation
from DataStructure.Map.Map import Map
import sys
sys.setrecursionlimit(100000) #例如这里设置为十万

"""
红黑树
"""
class RBTree(Map):
    RED = True
    BLACK = False
    class Node():
        key = None
        value = None
        # 左子树、右子树
        left = right = None
        color = True  # RED

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.color = True

    root = None
    size = 0
    res = ""

    def __init__(self):
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def isRed(self, node):
        """
        判断节点颜色
        :return:
        """
        if node == None:
            return self.BLACK
        return node.color

    def add(self, key, value):
        self.root = self.__add(self.root, key, value)
        # 最终根节点为黑色节点
        self.root.color = self.BLACK

    def __leftRotate(self, node):
        """
                node                                x
               /   \     向左旋转                  /  \
               T1   x  ------------->            node  T3
                   /  \                         /   \
                   T2  T3                       T1   T2
        :param node:
        :return:
        """
        x = node.right
        # 左旋转
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        return x

    def __rightRotate(self, node):
        """
         node                   x
        /   \     右旋转       /  \
       x    T2   ------->   y   node
      / \                       /  \
     y  T1                     T1  T2
        :param node:
        :return:
        """
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        return x

    def __flipColors(self, node):
        """
        颜色翻转
        :param node:
        :return:
        """
        node.color = self.RED
        node.left.color = self.BLACK
        node.right.color = self.BLACK

    """
   向node为根的红黑树中插入元素(k,v)，递归算法 
   返回插入新节点后红黑树的根
    """
    def __add(self, node, key, value):
        if node == None:
            self.size += 1
            return self.Node(key, value) # 默认插入红色节点
        if key < node.key:
            node.left = self.__add(node.left, key, value)
        elif key > node.key:
            node.right = self.__add(node.right, key, value)
        else: # key==node.key
            node.value = value

        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.__leftRotate(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.__rightRotate(node)

        if self.isRed(node.left) and self.isRed(node.right):
            self.__flipColors(node)
        return node

    # 返回以node为根节点的二分搜索树，key所在的节点
    def __getNode(self, node, key):
        if(node == None):
            return None
        if(key == node.key):
            return node
        if(key < node.key):
            return self.__getNode(node.left, key)
        else:
            return self.__getNode(node.right, key)

    def contains(self, key):
        return self.__getNode(self.root, key) != None

    def get(self, key):
        node = self.__getNode(self.root, key)
        return node.value if node != None else None

    def set(self, key, value):
        node = self.__getNode(self.root, key)
        if(node == None):
            print(str(key)+" doesn't exist!")
            return
        node.value = value

    """
    寻找二分搜索树的最小元素
    """
    def minxmum(self):
        return self.__minxmum(self.root).key

    def __minxmum(self, node):
        if (self.size == 0):
            print("BST is empty.")
            return
        if (node.left == None):
            return node
        return self.__minxmum(node.left)

    """
   从二分搜索树中删除最小值所在节点，并返回最小值
   """
    def removeMin(self):
        e = self.minxmum()
        self.root = self.__removeMin(self.root)
        return e

    def __removeMin(self, node):
        if (node.left == None):
            rightNode = node.right
            node.right = None
            self.size -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    """
    删除元素e
    """
    def remove(self, key):
        node = self.__getNode(self.root, key)
        if(node != None):
            self.root = self.__remove(self.root, key)
            return node
        return None

    def __remove(self, node, key):
        if (node == None):
            return None
        if (key < node.key):
            node.left = self.__remove(node.left, key)
            return node
        elif (key > node.key):
            node.right = self.__remove(node.right, key)
            return node
        else:
            if (node.left == None):
                nodeRight = node.right
                node.right = None
                self.size -= 1
                return nodeRight
            if (node.right == None):
                nodeLeft = node.left
                node.left = None
                self.size -= 1
                return nodeLeft
            # 否则存在左右两个子树
            successor = self.__minxmum(node.right)
            successor.right = self.__removeMin(node.right)
            successor.left = node.left
            node.left = node.right = None
            return successor

if __name__ == '__main__':
    filename = '../pride-and-prejudice.txt'
    words = FileOperation.readFile(filename)
    print(len(words))
    map = RBTree()
    for word in words:
        if(map.contains(word)):
            map.set(word, int(map.get(word))+1)
        else:
            map.add(word, 1)
    print("Total different words："+str(map.getSize()))
    print("Frequency of PRIDE："+str(map.get("pride")))
    print("Frequency of PREJUDICE："+str(map.get("prejudice")))