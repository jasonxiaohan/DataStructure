#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: AVLMap.py
@time: 2018/8/8 9:53
@desc:
"""

from DataStructure.AVLTree.AVLTree import AVLTree
from DataStructure.Map.Map import Map

class AVLMap(Map):
    def __init__(self):
        self.avl = AVLTree()

    def getSize(self):
        return self.avl.getSize()

    def isEmpty(self):
        return self.avl.isEmpty()

    def add(self, key, value):
        self.avl.add(key, value)

    def remove(self, key):
        return self.avl.remove(key)

    def contains(self, key):
        return self.avl.contains(key)

    def get(self, key):
        return self.avl.get(key)

    def set(self, key, value):
        self.avl.set(key, value)
