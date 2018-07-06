# -*- coding:utf-8 -*-
from DataStructure.Queue import Queue
class LoopQueue(Queue):
    __data = []
    __front, __tail = 0
    __size = 0

    def __init__(self, capacity=10):
        self.__data = [0 for i in range(capacity+1)]

    """
      获取队列的长度
      """
    def getSize(self):
        return self.__size

    """
    判断队列是否为空
    """
    def isEmpty(self):
        return self.__front == self.__tail

    def getCapacity(self):
        return len(self.__data)-1

    """
    入队列
    """
    def enqueue(self, e):
        if (self.__tail+1) % len(self.__data) == self.__front:
            pass
        pass

    def _resize(self, capacity):
        pass

    """
    出队列
    """
    def dequeue(self):
        pass

    """
    获取队首的元素
    """
    def getFront(self):
        pass

if __name__ == '__main__':
    loopQueue = LoopQueue()
