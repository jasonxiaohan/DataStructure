#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: Solution2-303.py
@time: 2018/7/29 14:41
@desc:
"""
class NumArray:
    __sum = [] # sum[i]存储前i个元素和,sum[0]=0
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__sum = [0 for i in range(len(nums)+1)]
        for i in range(1, len(self.__sum)):
            self.__sum[i] = self.__sum[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__sum[j+1] - self.__sum[i]

if __name__ == '__main__':
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(2, 5))
