#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018, Node Supply Chain Manager Corporation Limited.
@contact: jasonxiaohan198@qq.com
@file: Solution-349.py
@time: 2018/7/22 11:49
@desc:
"""

from DataStructure.Set.BSTSet import BSTSet

class Solution:
    def intersection(self, nums1, nums2):
        """
        :param nums1:
        :param nums2:
        :return:
        """
        list = []
        sets = set()
        for num1 in nums1:
            sets.add(num1)

        for num2 in nums2:
            if(num2 in sets):
                list.append(num2)
                sets.remove(num2)
        return list

if __name__ == '__main__':
    num1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    list = solution.intersection(num1, nums2)
    print(list)

