#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018, Node Supply Chain Manager Corporation Limited.
@contact: jasonxiaohan198@qq.com
@file: MaxHeap.py
@time: 2018/7/23 7:57
@desc:
"""

"""
最大堆
"""
class MaxHeap:
    data = None

    def __init__(self, capacity=10):
        self.data = [0 for i in range(capacity)]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.data == None

    def __parent(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
        :param index:
        :return:
        """
        if(index == 0):
            print("index-0 doesn't have parent.")
            return
        return (index - 1)/2

    def __leftChild(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子节点的索引
        :param index:
        :return:
        """
        return int(2 * index ) + 1

    def __rightChild(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子节点的索引
        :param index:
        :return:
        """
        return int(2 * index) + 2