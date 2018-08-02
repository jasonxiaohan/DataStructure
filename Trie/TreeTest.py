# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 18:34
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : TreeTest.py
# @Software: PyCharm
from DataStructure.Set.BSTSet import BSTSet
from DataStructure.Trie.Trie import Trie
from DataStructure.FileOperation import FileOperation
import time

if __name__ == '__main__':
    words = FileOperation.readFile('../pride-and-prejudice.txt')
    print("Total word："+str(len(words)))
    starTime = time.clock()
    set = BSTSet()
    for word in words:
        set.add(word)
    for word in words:
        set.contains(word)
    endTime = time.clock()
    print("Total different words："+str(set.getSize()))
    print("BSTSet："+str(endTime-starTime)+" s ")

    # Trie
    starTime = time.clock()
    trie = Trie()
    for word in words:
        trie.add(word)
    for word in words:
        trie.contains(word)
    endTime = time.clock()
    print("Total different words：" + str(trie.getSize()))
    print("Trie：" + str(endTime - starTime) + " s ")