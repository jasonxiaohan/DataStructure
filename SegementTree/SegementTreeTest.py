#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: SegementTreeTest.py
@time: 2018/7/28 23:17
@desc:
"""
from DataStructure.SegementTree.Merger import Merger
from DataStructure.SegementTree.SegementTree import SegementTree

class SegementTreeTest(Merger):
    def merge(self, a, b):
        return int(a+b)
if __name__ == '__main__':
    nums = [1,3,5]
    segTest = SegementTreeTest()
    segTree = SegementTree(nums, segTest)
    print(segTree)

    result = segTree.query(0, 2)
    print(result)
    result = segTree.query(2, 5)
    print(result)
    segTree.set(1, 2)
    result = segTree.query(0, 2)
    print(result)
