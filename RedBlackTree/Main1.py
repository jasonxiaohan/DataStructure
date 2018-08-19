#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: Main1.py
@time: 2018/8/19 14:57
@desc:
"""
import random,time
from DataStructure.BST.BinarySearchTree import BinarySearchTree
from DataStructure.AVLTree.AVLTree import AVLTree
from DataStructure.RedBlackTree.RBTree import RBTree

if __name__ == '__main__':
    n = 2000000
    testData = []
    for i in range(n):
        testData.append(random.randint(0, 10000000))

    # 测试bst
    bst = BinarySearchTree()
    startTime = time.clock()
    for x in testData:
        bst.add(x, None)
    endTime = time.clock()

    time1 = (endTime - startTime)
    print("BST："+str(time1)+" s")

    # 测试avl
    avl = AVLTree()
    startTime = time.clock()
    for x in testData:
        avl.add(x, None)
    endTime = time.clock()

    time2 = (endTime - startTime)
    print("AVL：" + str(time2) + " s")

    # 测试redTree
    rb = RBTree()
    startTime = time.clock()
    for x in testData:
        rb.add(x, None)
    endTime = time.clock()
    time3 = (endTime - startTime)
    print("RBTree：" + str(time3) + " s")
