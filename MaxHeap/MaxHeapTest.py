# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 14:21
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : MaxHeapTest.py
# @Software: PyCharm

import time
import random
from DataStructure.MaxHeap.MaxHeap import MaxHeap

class MaxHeapTest:
    @staticmethod
    def testHeap(testData, isHeapify=False):
        startTime = time.clock()
        if(isHeapify):
            maxHeap = MaxHeap(0, testData)
        else:
            maxHeap = MaxHeap()
            for i in range(len(testData)):
                maxHeap.add(i)

        data = []
        for i in range(len(testData)):
            data.append(maxHeap.extractMax())

        for i in range(1, len(testData)):
            if (data[i - 1] < data[i]):
                try:
                    raise Exception("Error:" + str(data[i - 1]) + "," + str(data[i]))
                except Exception as err:
                    print("An exception：" + str(err))
        print("Test MaxHeap completed.")

        endTime = time.clock()
        return endTime - startTime

if __name__ == '__main__':
    n = 100000
    testData = []
    for i in range(n):
        testData.append(random.randint(0, 10000000))

    time1 = MaxHeapTest.testHeap(testData, False)
    print("Without heapify："+str(time1)+" s ")

    time2 = MaxHeapTest.testHeap(testData, True)
    print("With heapify："+str(time2) +" s ")
