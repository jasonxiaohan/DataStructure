# -*- coding:utf-8 -*-
from DataStructure.Queue import Queue
from DataStructure.Array import Array
"""
队列实现类
"""
class ArrayQueue(Queue):
    def __init__(self, capacity=10):
        self.__array = Array(capacity)

    def __str__(self):
        res = ('Queue:size = %d，capacity = %d\n') % (self.__array.getSize(), self.__array.getCapacity())
        res += "fron ["
        for i in range(self.__array.getSize()):
            res += str(self.__array.get(i))
            if i != self.__array.getSize() - 1:
                res += ", "
        res += "] tail"
        return res

    """
    获取队列的长度
    """
    def getSize(self):
        return self.__array.getSize()

    """
    判断队列是否为空
    """
    def isEmpty(self):
        return self.__array.isEmpty()

    def getCapacity(self):
        return self.__array.getCapacity()

    """
    入队列
    """
    def enqueue(self, e):
        self.__array.addLast(e)

    """
    出队列
    """
    def dequeue(self):
        return self.__array.removeFirst()

    """
    获取队首的元素
    """
    def getFront(self):
        return self.__array.getFirst()

if __name__ == '__main__':
    queue = ArrayQueue()
    queue.enqueue(11)
    queue.enqueue(22)
    queue.enqueue(33)
    print(queue)
    queue.dequeue()
    print(queue)