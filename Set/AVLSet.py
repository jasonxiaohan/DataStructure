#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: AVLSet.py
@time: 2018/8/8 10:02
@desc:
"""
from DataStructure.AVLTree.AVLTree import AVLTree
from DataStructure.Set.Set import Set

class AVLSet(Set):
    def __init__(self):
        self.avl = AVLTree()
    def getSize(self):
        return self.avl.getSize()
    def isEmpty(self):
        return self.avl.isEmpty()
    def add(self, e):
        self.avl.add(e, None)
    def contains(self, e):
        return self.avl.contains(e)
    def remove(self, e):
        self.avl.remove(e)