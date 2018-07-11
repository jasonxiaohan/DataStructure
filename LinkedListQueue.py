# -*- coding:utf-8 -*-
from DataStructure.Queue import Queue

"""
使用链表实现队列
"""

class LinkedListQueue(Queue):
    # 节点设计成内部类
    class __Node:
        e = None
        next = None

        def __init__(self, e, next=None):
            self.e = e
            self.next = next

        def __str__(self):
            return str(self.e)
    __head = None
    __tail = None
    __size = 0

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    """
    获取队列的长度
    """
    def getSize(self):
        return self.__size

    """
    判断队列是否为空
    """
    def isEmpty(self):
        return self.__size == 0

    """
    入队列
    """
    def enqueue(self, e):
        if self.__tail == None:
            self.__tail = self.__Node(e)
            self.__head = self.__tail
        else:
            self.__tail.next = self.__Node(e)
            self.__tail = self.__tail.next
            self.__size += 1

    """
    出队列
    """
    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue from an empty queue.")
            return
        retNode = self.__head
        self.__head = self.__head.next
        retNode.next = None
        if self.__head == None:
            self.__tail = None
        self.__size -= 1
        return retNode.e

    """
    获取队首的元素
    """
    def getFront(self):
        if self.isEmpty():
            print("Cannot dequeue from an empty queue.")
            return
        return self.__head.e

    def __str__(self):
        res = "Queue：front "
        cur = self.__head
        while cur != None:
            res += str(cur) + "->"
            cur = cur.next
        res += "NULL tail"
        return res
if __name__ == '__main__':
    linkedListQueue = LinkedListQueue()
    for i in range(10):
        linkedListQueue.enqueue(i)
        print(linkedListQueue)

        if i % 3 == 2:
            linkedListQueue.dequeue()
            print(linkedListQueue)
