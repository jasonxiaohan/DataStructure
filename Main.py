# -*- coding:utf-8 -*-

import time
import random
from DataStructure.ArrayQueue import ArrayQueue
from DataStructure.LoopQueue import LoopQueue

from DataStructure.ArrayStack import ArrayStack
from DataStructure.LinkedListStack import LinkedListStack

"""

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

    """
    测试使用stack运行opCount个push和pop操作所需要的时间，单位：秒
    """
    def _testStack(self, stack, opCount):
        startTime = time.clock()
        for i in range(opCount):
            stack.push(random.randint(0, 10000000000))
        for i in range(opCount):
            stack.pop()
        endTime = time.clock()
        return endTime - startTime

if __name__ == '__main__':
    opCount = 10000
    main = Main()
    """
    arrayQueue = ArrayQueue()
    time1 = main._testQueue(arrayQueue, opCount)
    print("ArrayQueue,time："+str(time1) +"s")

    loopQueue = LoopQueue()
    time2 = main._testQueue(loopQueue, opCount)
    print("LoopQueue,time："+str(time2) +"s")
    """
    # 测试队列与循环队列执行的效率

    # 测试stack
    arrayStack = ArrayStack()
    time1 = main._testStack(arrayStack, opCount)
    print("ArrayStack,time："+str(time1)+"s")

    linkedListStack = LinkedListStack()
    time2 = main._testStack(linkedListStack, opCount)
    print("LinkedListStack,time："+str(time2)+"s")
