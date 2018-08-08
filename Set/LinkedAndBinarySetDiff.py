# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 12:05
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : LinkedAndBinarySetDiff.py
# @Software: PyCharm
import time
from DataStructure.FileOperation import FileOperation
from DataStructure.Set.LinkedListSet import LinkedListSet
from DataStructure.Set.BSTSet import BSTSet
from DataStructure.Set.AVLSet import AVLSet

"""
链表、二分搜索树实现集合，
两者性能进行对比
words = FileOperation.readFile('./pride-and-prejudice.txt')
print("Total words："+str(len(words)))
set = BSTSet() #LinkedListSet()
for word in words:
    set.add(word)
print("Total different words: "+str(set.getSize()))
"""

class LinkedAndBinarySetDiff:
    """
    """
    @staticmethod
    def _testQueue(set, filename):
        startTime = time.clock()
        words = FileOperation.readFile(filename)
        print("Total words："+str(len(words)))
        for word in words:
            set.add(word)
        print("Total different words："+str(set.getSize()))
        endTime = time.clock()
        return endTime - startTime

if __name__ == '__main__':
    filename = '../pride-and-prejudice.txt'
    bstSet = BSTSet()
    time1 = LinkedAndBinarySetDiff._testQueue(bstSet, filename)
    print("BST Set："+str(time1)+"s")

    linkSet = LinkedListSet()
    time2 = LinkedAndBinarySetDiff._testQueue(linkSet, filename)
    print("LinkedList Set："+str(time2)+"s")

    avlSet = AVLSet()
    time3 = LinkedAndBinarySetDiff._testQueue(avlSet, filename)
    print("AVL Set：" + str(time3) + "s")