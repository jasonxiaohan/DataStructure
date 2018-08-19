#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: RBTreeAndAVLDiff.py
@time: 2018/8/19 14:42
@desc:
"""
import time
from DataStructure.FileOperation import FileOperation
from DataStructure.AVLTree.AVLTree import AVLTree
from DataStructure.RedBlackTree.RBTree import RBTree
from DataStructure.BST.BinarySearchTree import BinarySearchTree

class RBTreeAndAVLDiff:
    def _test(tree, filename):
        startTime = time.clock()
        words = FileOperation.readFile(filename)
        print("Total words："+str(len(words)))
        # words.sort()
        for word in words:
            if (tree.contains(word)):
                tree.set(word, int(tree.get(word)) + 1)
            else:
                tree.add(word, 1)
        for word in words:
            tree.contains(word)

        print("Total different words："+str(tree.getSize()))
        endTime = time.clock()
        return endTime - startTime

if __name__ == '__main__':
    filename = '../pride-and-prejudice.txt'
    redTree = RBTree()
    time1 = RBTreeAndAVLDiff._test(redTree, filename)
    print("RBTree ："+str(time1)+"s")

    avlTree = AVLTree()
    time2 = RBTreeAndAVLDiff._test(avlTree, filename)
    print("AVLTree ："+str(time2)+"s")