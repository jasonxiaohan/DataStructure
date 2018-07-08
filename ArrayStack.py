# -*- coding:utf-8 -*-
from DataStructure.Stack import Stack
from DataStructure.Array import Array

"""
栈
"""
class ArrayStack(Stack):
    data = []
    def __init__(self, capacity=10):
        self.array = Array(capacity)

    def __str__(self):
        res = ('Stack:size = %d，capacity = %d\n') % (self.array.getSize(), self.array.getCapacity())
        res += "["
        for i in range(self.array.getSize()):
            res += str(self.array.get(i))
            if i != self.array.getSize() - 1:
                res += ","
        res += "] top"
        return res

    def getSize(self):
        return self.array.getSize()

    def isEmpty(self):
        return self.array.isEmpty()

    def getCapacity(self):
        return self.array.getCapacity()

    def push(self, e):
        self.array.addLast(e)

    def pop(self):
        return self.array.removeLast()

    def peek(self):
        return self.array.getLast()

if __name__ == '__main__':
    arrayStack = ArrayStack()
    arrayStack.push(11)
    arrayStack.push(22)
    arrayStack.push(33)
    arrayStack.push(44)
    arrayStack.push(55)
    print(arrayStack)
    arrayStack.pop()
    print(arrayStack)
    arrayStack.pop()
    print(arrayStack)