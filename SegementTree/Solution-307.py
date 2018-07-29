#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: Solution-307.py
@time: 2018/7/29 15:10
@desc:
"""

class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__data = [nums[i] for i in range(len(nums))]
        self.__sum = [0 for i in range(len(nums)+1)]

        for i in range(1, len(self.__sum)):
            self.__sum[i] = self.__sum[i-1] + nums[i-1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.__data[i] = val
        for index in range(i+1, len(self.__sum)):
            self.__sum[index] = self.__sum[index-1] + self.__data[index-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__sum[j+1] - self.__sum[i]
if __name__ == '__main__':
    numArray = NumArray([1, 3, 5])
    print(numArray.sumRange(0, 2))
    numArray.update(1, 2)
    print(numArray.sumRange(0, 2))
