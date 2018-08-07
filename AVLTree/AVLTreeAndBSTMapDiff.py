# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 18:18
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : AVLTreeAndBSTMapDiff.py
# @Software: PyCharm

import time
from DataStructure.FileOperation import FileOperation
from DataStructure.AVLTree.AVLTree import AVLTree
from DataStructure.Map.BSTMap import BSTMap

"""
AVLTree与二分搜索树性能进行比较
"""
class AVLTreeAndBSetMapDiff:
    """
    """
    @staticmethod
    def _testQueue(map, filename):
        startTime = time.clock()
        words = FileOperation.readFile(filename)
        print("Total words："+str(len(words)))
        # words.sort()
        for word in words:
            if (map.contains(word)):
                map.set(word, int(map.get(word)) + 1)
            else:
                map.add(word, 1)
        for word in words:
            map.contains(word)
        for word in words:
            map.remove(word)
            try:
                if not map.isBST() or not map.isBalanced():
                    raise Exception("Error")
            except Exception as err:
                print(err)

        print("Total different words："+str(map.getSize()))
        endTime = time.clock()
        return endTime - startTime

if __name__ == '__main__':
    filename = '../pride-and-prejudice.txt'
    # bstMap = BSTMap()
    # time1 = AVLTreeAndBSetMapDiff._testQueue(bstMap, filename)
    # print("BST Map："+str(time1)+"s")

    avlTree = AVLTree()
    time2 = AVLTreeAndBSetMapDiff._testQueue(avlTree, filename)
    print("AVLTree Map："+str(time2)+"s")