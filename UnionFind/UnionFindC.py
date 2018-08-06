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

class UnionFindC(UF):
    def __init__(self, size):
        self.__parent = [x for x in range(size)]
        self.__sz = [1 for x in range(size)]  # sz[i]表是以i为根的集合中元素个数

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
        if self.__sz[pRoot] < self.__sz[qRoot]:
            self.__parent[pRoot] = qRoot
            self.__sz[qRoot] += self.__sz[pRoot]
        else:
            self.__parent[qRoot] = pRoot
            self.__sz[pRoot] += self.__sz[qRoot]

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