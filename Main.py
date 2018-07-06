# -*- coding:utf-8 -*-

import time
import random
from DataStructure.Queue import Queue
from DataStructure.ArrayQueue import ArrayQueue
from DataStructure.LoopQueue import LoopQueue

"""
测试队列与循环队列执行的效率
"""
class Main():
    """
    测试使用q运行opCount个enqueue和dequeue操作所需的时间，单位：秒
    """
    def _testQueue(self,q, opCount):
        startTime = time.clock()
        for i in range(opCount):
            q.enqueue(random.randint(0, 10000000000))
        for i in range(opCount):
            q.dequeue()
        endTime = time.clock()
        return endTime - startTime

if __name__ == '__main__':
    opCount = 10000
    arrayQueue = ArrayQueue()
    main = Main()
    time1 = main._testQueue(arrayQueue, opCount)
    print("ArrayQueue,time："+str(time1) +"s")

    loopQueue = LoopQueue()
    time2 = main._testQueue(loopQueue, opCount)
    print("LoopQueue,time："+str(time2) +"s")
