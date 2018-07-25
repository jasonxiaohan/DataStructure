# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 18:15
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : Solution-347.py
# @Software: PyCharm

from DataStructure.MaxHeap.PriorityQueue import PriorityQueue

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
        pq = PriorityQueue()
        for key in dict.keys():
            if pq.getSize() < k:
                pq.enqueue(self.Freq(key, dict[key]))
            elif dict[key] > pq.getFront().freq:
                pq.dequeue()
                pq.enqueue(self.Freq(key, dict[key]))
        list = []
        while not pq.isEmpty():
            d = pq.dequeue().e
            list.append(d)
        return list


if __name__ == '__main__':
    solution = Solution()
    dict = solution.topKFrequent([1,1,1,2,2,3,4], 3)
    print(dict)