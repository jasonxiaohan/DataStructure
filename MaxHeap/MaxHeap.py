#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: MaxHeap.py
@time: 2018/7/23 7:57
@desc:
"""
from DataStructure.Array import Array
import random

"""
最大堆
"""
class MaxHeap:
    __data = None

    def __init__(self, capacity=10, arr=None):
        self.__data = Array(capacity, arr)
        if(arr != None):
            for i in range(int(len(arr)-1), -1, -1):
                self.__siftDown(i)

    def size(self):
        return self.__data.getSize()

    def isEmpty(self):
        return self.__data.getSize() == 0

    def __parent(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
        :param index:
        :return:
        """
        try:
            if(index == 0):
                raise Exception("index-0 doesn't have parent.");
        except Exception as err:
            print(err)
        return int((index - 1)/2)

    def __leftChild(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
        :param index:
        :return:
        """
        return int(2 * index) + 1

    def __rightChild(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
        :param index:
        :return:
        """
        return int(2 * index) + 2

    def add(self, e):
        """
        向堆中添加元素
        :param e:
        :return:
        """
        self.__data.addLast(e)
        self.__siftUp(int(self.__data.getSize() - 1))

    def __siftUp(self, k):
        while(k > 0 and self.__data.get(self.__parent(k)) < self.__data.get(k)):
            self.__data.swap(k, self.__parent(k))
            k = self.__parent(k)

    def findMax(self):
        """
        看堆中最大元素
        :return:
        """
        try:
            if(self.__data.getSize() == 0):
                raise  Exception("Can not findMax when heap is empty.")
        except Exception as err:
            print(err)
        return self.__data.get(0)

    def extractMax(self):
        """
        取出堆中最大元素
        :return:
        """
        ret = self.findMax()
        self.__data.swap(0, int(self.__data.getSize() - 1))
        self.__data.removeLast()
        self.__siftDown(0)
        return ret

    def __siftDown(self, k):
        while(self.__leftChild(k) < self.__data.getSize()):
            j = self.__leftChild(k)
            if(int(j + 1) < self.__data.getSize() and self.__data.get(int(j+1)) > self.__data.get(int(j))) :
                j += 1

            # self.__data[j] 是leftChild 和 rightChild 中的最大值
            if(self.__data.get(k) > self.__data.get(j)):
                break
            self.__data.swap(k, j)
            k = j

    def replace(self, e):
        """
        取出堆中的最大元素，并将取出的元素替换成：e
        :param e:
        :return:
        """
        ret = self.findMax()
        self.__data.set(0, e)
        self.__siftDown(0)
        return ret

    def __str__(self):
        """
        将类的实例变成str
        :return:
        """
        res = ('Array:size = %d，capacity = %d\n') % (self.size(),self.__data.getCapacity())
        res += "["
        for i in range(self.size()):
            res += str(self.__data.get(i))
            if i != self.size() - 1:
                res += ","
        res += "]"
        return res
if __name__ == '__main__':
    n = 100
    maxHeap = MaxHeap()
    for i in range(n):
        maxHeap.add(random.randint(0, 10000000))
    data = []
    for i in range(n):
        data.append(maxHeap.extractMax())
    print(data)

    for i in range(1, n):
        if(data[i - 1] < data[i]):
            try:
                raise Exception("Error:"+str(data[i-1])+","+str(data[i]))
            except Exception as err:
                print("An exception："+str(err))
    print("Test MaxHeap completed.")