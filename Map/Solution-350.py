#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018, Node Supply Chain Manager Corporation Limited.
@contact: jasonxiaohan198@qq.com
@file: Solution-350.py
@time: 2018/7/22 12:00
@desc:
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        for num2 in nums2:
            if(num2 in nums1):
                if(dict.get(num2)) != None:
                    dict[num2] = int(dict.get(num2)+1)
                else:
                    dict[num2] = 1
                nums1.remove(num2)
        list = []
        for k in dict:
            l = []
            l.append(k)
            list = list + l*dict[k]
        return list

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [1, 2, 3]

    dict = solution.intersect(nums1, nums2)
    print(dict)
