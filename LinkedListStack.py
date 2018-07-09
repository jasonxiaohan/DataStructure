# -*- coding:utf-8 -*-
from DataStructure.Stack import Stack
from DataStructure.LinkedList import LinkedList

class LinkedListStack(Stack):
    __list = [];
    def __init__(self):
        self.__list = LinkedList()

    def getSize(self):
        return self.__list.getSize()

    def isEmpty(self):
        return self.__list.isEmpty()

    def push(self, e):
        self.__list.addFirst(e)

    def pop(self):
        return self.__list.removeFirst()

    def peek(self, e):
        return self.__list.getFirst()

    def __str__(self):
        res = ('Stack：top ')
        res += str(self.__list)
        return res

if __name__ == '__main__':
     stack = LinkedListStack()
     for i in range(5):
         stack.push(i)
         print(stack)
     stack.pop()
     print(stack)

