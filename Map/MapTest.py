#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018, Node Supply Chain Manager Corporation Limited.
@contact: jasonxiaohan198@qq.com
@file: BSTMapTest.py
@time: 2018/7/22 11:20
@desc:
"""
from DataStructure.FileOperation import FileOperation
from DataStructure.Map.BSTMap import BSTMap
from DataStructure.Map.LinkedListMap import LinkedListMap
import time

class MapTest:
    @staticmethod
    def testMap(map, filename):
        startTime = time.clock()
        words = FileOperation.readFile(filename)
        print("Total words：" + str(len(words)))
        for word in words:
            if(map.contains(word)):
                map.set(word, int(map.get(word))+1)
            else:
                map.add(word, 1)
        print("Total different words：" + str(map.getSize()))
        endTime = time.clock()
        return endTime - startTime

if __name__ == '__main__':
    filename = '../pride-and-prejudice.txt'
    bstMap = BSTMap()
    time1 = MapTest.testMap(bstMap, filename)
    print("BST Map："+str(time1)+" s")
    linkedMap = LinkedListMap()
    time2 = MapTest.testMap(linkedMap,filename)
    print("LinkedList Map："+str(time2)+" s")
