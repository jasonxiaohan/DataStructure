# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 18:15
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : Solution-347.py
# @Software: PyCharm

from DataStructure.MaxHeap.PriorityQueue import PriorityQueue
import operator

class Solution:
    class Freq:
        e = freq = None
        def __init__(self, e, freq):
            self.e = e
            self.freq = freq

        def compareTo(self, another):
            if self.freq < another.freq:
                return 1
            elif self.freq > another.freq:
                return -1
            else:
                return 0

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] = int(dict.get(num)+1)
            else:
                dict[num] = 1
        dictSort = sorted(dict.items(), key = operator.itemgetter(1), reverse = True)
        list = []
        for d in dictSort:
            if len(list) < k:
                list.append(d[0])
            else:
                break
        return list


if __name__ == '__main__':
    solution = Solution()
    dict = solution.topKFrequent([1,2,2,1,1,3], 2)
    print(dict)