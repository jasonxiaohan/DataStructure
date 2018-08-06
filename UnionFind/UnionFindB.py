#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: UnionFindB.py
@time: 2018/8/5 15:27
@desc:
"""

from DataStructure.UnionFind.UF import UF

class UnionFindB(UF):
    def __init__(self, size):
        self.__parent = [x for x in range(size)]

    def getSize(self):
        return len(self.__parent)

    def isConnected(self, p, q):
        """
        查找元素p和q是否所属一个集合
        O(h)复杂度，h为树的高度
        :param p:
        :param q:
        :return:
        """
        return  self.find(p) == self.find(q)

    def unionElements(self, p, q):
        """
        合并元素p和元素q所属的集合
        O(h)复杂度，h为树的高度
        :param p:
        :param q:
        :return:
        """
        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot == qRoot:
            return
        self.__parent[pRoot] = qRoot

    def find(self, p):
        """
        查找过程，查找元素p所对应的集合编号
        O(h)复杂度，h为树的高度
        :param p:
        :return:
        """
        try:
            if p < 0 and p >= len(self.__parent):
                raise Exception("p is out of bound.")
        except Exception as err:
            print(err)
            return
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p