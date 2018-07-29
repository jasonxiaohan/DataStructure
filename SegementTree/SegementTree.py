#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: SegementTree.py
@time: 2018/7/28 16:40
@desc: 线段树
"""
from DataStructure.SegementTree.Merger import Merger

class SegementTree(Merger):
    def __init__(self, arr, merger):
        self.data = [arr[i] for i in range(len(arr)) ]
        self.tree = [None for i in range(4*len(arr))]
        self.merger = merger

        self.__buildSegmentTree(0, 0, int(len(arr)-1))

    def __buildSegmentTree(self, treeIndex, l, r):
        """
        在treeIndex的位置创建表示区间[l....r]的线段树
        :param treeIndex:
        :param l:
        :param r:
        :return:
        """
        if l == r:
            self.tree[treeIndex] = self.data[l]
            return
        leftTreeIndex = self.leftChild(treeIndex)
        rightTreeIndex = self.rightChild(treeIndex)

        mid = int(l + (r - l) / 2)
        self.__buildSegmentTree(leftTreeIndex, l, mid)
        self.__buildSegmentTree(rightTreeIndex, int(mid+1), r)
        self.tree[treeIndex] = self.merger.merge(self.tree[leftTreeIndex], self.tree[rightTreeIndex])

    def get(self, index):
        try:
            if index < 0 or index >= len(self.data):
                raise Exception("Index is illegal.")
        except Exception as e:
            print(e)
        return self.data[index]

    def getSize(self):
        return len(self.data)

    def leftChild(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素左孩子节点的索引
        :param index:
        :return:
        """
        return int((2*index) + 1)

    def rightChild(self, index):
        """
        返回完全二叉树的数组表示中，一个索引所表示的元素右孩子节点的索引
        :param index:
        :return:
        """
        return int((2*index) + 2)

    def query(self, queryL, queryR):
        """
        返回区间[queryL, queryR]的值
        :param queryL:
        :param queryR:
        :return:
        """
        try:
            if queryL < 0 or queryL >= len(self.data) or queryR < 0 or queryR >= len(self.data) or queryL > queryR:
                raise Exception("Index is illegal.")
        except Exception as e:
            print(e)
            return
        return self.__query(0, 0, len(self.data)-1, queryL, queryR)

    def __query(self, treeIndex, l, r, queryL, queryR):
        """
        在以treeID为根的线段树中[l....r]的范围里，搜索区间[queryL,queryR]的值
        :param treeIndex:
        :param l:
        :param r:
        :param queryL:
        :param queryR:
        :return:
        """
        if l == queryL and r == queryR:
            return self.tree[treeIndex]
        mid = int(l + (r - l) / 2)
        leftTreeIndex = self.leftChild(treeIndex)
        rightTreeIndex = self.rightChild(treeIndex)

        if queryL >= int(mid + 1):
            return self.__query(rightTreeIndex, mid+1, r, queryL, queryR)
        elif queryR <= mid:
            return self.__query(leftTreeIndex, l, mid, queryL, queryR)

        leftResult = self.__query(leftTreeIndex, l, mid, queryL, mid)
        rightResult = self.__query(rightTreeIndex, mid + 1, r, mid + 1, queryR)
        return self.merger.merge(leftResult, rightResult)

    def set(self, index ,e):
        """
        将index位置的值，更新为e
        :param index:
        :param e:
        :return:
        """
        self.__set(0, 0, len(self.data)-1, index, e)

    def __set(self, treeIndex, l, r, index, e):
        """
        以treeIndex为根的线段树中更新index的值为e
        :param treeIndex:
        :param l:
        :param r:
        :param index:
        :param e:
        :return:
        """
        if l == r:
            self.tree[treeIndex] = e
            return

        leftTreeIndex = self.leftChild(treeIndex)
        rightTreeIndex = self.rightChild(treeIndex)
        mid = int(l + (r - l) / 2)

        if index >= (mid+1):
            self.__set(rightTreeIndex, mid+1, r, index, e)
        else:
            self.__set(leftTreeIndex, l, mid, index, e)
        self.tree[treeIndex] = self.merger.merge(self.tree[leftTreeIndex], self.tree[rightTreeIndex])

    def __str__(self):
        res = "["
        for index, data in enumerate(self.tree):
            if data != None:
                res += str(data)
            else:
                res += str('null')
            if index != int(len(self.tree) -1):
                res += str(' , ')
        res += str(']')
        return res