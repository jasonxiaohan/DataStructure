# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 16:37
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : PriorityQueue.py
# @Software: PyCharm

from DataStructure.Queue import Queue
from DataStructure.MaxHeap.MaxHeap import MaxHeap

"""
优先队列
"""
class PriorityQueue(Queue):
    __maxHeap = None
    def __init__(self):
        self.__maxHeap = MaxHeap()

    def getSize(self):
        return self.__maxHeap.size()

    def isEmpty(self):
        return self.__maxHeap.isEmpty()

    def getFront(self):
        return self.__maxHeap.findMax()

    def enqueue(self, e):
        self.__maxHeap.add(e)

    def dequeue(self):
        return self.__maxHeap.extractMax()
