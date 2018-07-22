#!/usr/bin/env python
# encoding: utf-8
'''
@author: daixiaohan
@license: (C) Copyright 2018, Node Supply Chain Manager Corporation Limited.
@contact: jasonxiaohan198@qq.com
@file: LinkedListMap.py
@time: 2018/7/21 16:33
@desc:
'''

from DataStructure.FileOperation import FileOperation
from DataStructure.Map.Map import Map

"""
使用链表实现map（映射）
"""
class LinkedListMap(Map):

    # 节点设计成内部类
    class __Node:
        key = None
        value = None
        next = None

        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.key+" : "+self.value)

    # 虚拟头节点
    __dummyHead = None
    __size = 0

    def __init__(self):
        self.__dummyHead = self.__Node(None, None, None)
        self.__size = 0

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def __getNode(self, key):
        cur = self.__dummyHead.next
        while(cur != None):
            if(cur.key == key):
                return cur
            cur = cur.next
        return None

    def contains(self, key):
        return self.__getNode(key)

    def get(self, key):
        node = self.__getNode(key)
        return node.value if node != None else 0

    def add(self, key, value):
        node = self.__getNode(key)
        if(node == None):
            self.__dummyHead.next = self.__Node(key, value, self.__dummyHead.next)
            self.__size += 1
        else:
            node.value = value

    def set(self, key, value):
        node = self.__getNode(key)
        if(node == None):
            print(str(key)+" doesn't exist!")
            return
        else:
            node.value = value

    def remove(self, key):
        prev = self.__dummyHead
        while(prev.next != None):
            if(prev.next.key == key):
                break
            prev = prev.next
        if(prev.next != None):
            delNode = prev.next
            prev.next = delNode.next
            delNode.next = None
            self.__size -= 1
            return delNode.value
        return None

# if __name__ == '__main__':
#     filename = '../pride-and-prejudice.txt'
#     words = FileOperation.readFile(filename)
#     print(len(words))
#     map = LinkedListMap()
#     for word in words:
#         if(map.contains(word)):
#             map.set(word, int(map.get(word))+1)
#         else:
#             map.add(word, 1)
#     print("Total different words："+str(map.getSize()))
#     print("Frequency of PRIDE："+str(map.get("pride")))
#     print("Frequency of PREJUDICE："+str(map.get("prejudice")))
