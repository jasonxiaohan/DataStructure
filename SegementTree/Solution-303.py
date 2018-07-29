#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: Solution-303.py
@time: 2018/7/29 14:23
@desc:
"""
from DataStructure.SegementTree.SegementTree import SegementTree

class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) > 0:
            self.segmentTree = SegementTree(nums, self)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        try:
            if self.segmentTree == None:
                raise Exception("Segment is null.");
        except Exception as e:
            print(e)
            return
        return self.segmentTree.query(i,j)

    def merge(self, a, b):
        return int(a + b)
if __name__ == '__main__':
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(2, 5))