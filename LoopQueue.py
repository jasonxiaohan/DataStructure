# -*- coding:utf-8 -*-
from DataStructure.Queue import Queue
class LoopQueue(Queue):
    __data = []
    # __front：队首 __tail：队尾
    __front = 0
    __tail = 0
    # __size：队列的长度
    __size = 0

    def __init__(self, capacity=10):
        self.__data = [0 for i in range(capacity+1)]

    """
    将类的实例变成str
    """
    def __str__(self):
        res = ('Queue:size = %d，capacity = %d\n') % (self.__size, self.getCapacity())
        res += "front ["
        i = self.__front
        while True:
            if i == self.__tail:
                break
            res += str(self.__data[i])
            if int(i + 1) % len(self.__data) != self.__tail:
                res += ", "
            i = int((i + 1) % len(self.__data))
        res += "] tail"
        return res

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
        # 判断队列是否已满
        if (self.__tail + 1) % len(self.__data) == self.__front:
            self._resize(self.getCapacity() * 2)
        self.__data[self.__tail] = e
        self.__tail = (self.__tail + 1) % len(self.__data)
        self.__size += 1

    """
    出队列
    """
    def dequeue(self):
        if not self.__data:
            print("Cannot dequeue from an empty queue.")
            return
        ret = self.__data[self.__front]
        self.__data[self.__front] = 0
        self.__front = (self.__front + 1 ) % len(self.__data)
        self.__size -= 1
        if self.__size == int(self.getCapacity() / 4) and int(self.getCapacity() / 2) != 0:
            self._resize(int(self.getCapacity() / 2))
        return ret

    def _resize(self, capacity):
        _newData = [0 for i in range(capacity + 1)]
        for i in range(self.__size):
            _newData[i] = self.__data[(i + self.__front) % len(self.__data)]
        self.__data = _newData
        self.__front = 0
        self.__tail = self.__size

    """
    获取队首的元素
    """
    def getFront(self):
        if(self.isEmpty()):
            print("Queue is empty.")
            return
        return self.__data[self.__front]

if __name__ == '__main__':
    loopQueue = LoopQueue()
    for i in range(10):
        loopQueue.enqueue(i)
        print(loopQueue)
        if i % 3 == 2:
            loopQueue.dequeue()
            print(loopQueue)
    """
    loopQueue.enqueue(11)
    print(loopQueue)
    loopQueue.enqueue(22)
    loopQueue.enqueue(33)
    print(loopQueue)
    loopQueue.dequeue()
    print(loopQueue)
    loopQueue.dequeue()
    print(loopQueue)
    """
