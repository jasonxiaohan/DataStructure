#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: UnionFindE.py
@time: 2018/8/5 18:21
@desc:
"""

from DataStructure.UnionFind.UF import UF

"""
路径压缩
"""
class UnionFindE(UF):
    def __init__(self, size):
        self.__parent = self.__rank = [x for x in range(size)] # rank[i]表是以i为根的集合所表示的树的层数

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
        查找过程，查找元素p所对应的集合编号
        O(h)复杂度，h为树的高度
        :param p:
        :param q:
        :return:
        """
        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot == qRoot:
            return
        # 根据两个元素所在树的rank不同判断合并方向
        # 将rank低的集合合并到rank高的集合上
        if self.__rank[pRoot] < self.__rank[qRoot]:
            self.__parent[pRoot] = qRoot
        elif self.__rank[qRoot] < self.__rank[pRoot]:
            self.__parent[qRoot] = pRoot
        else:
            self.__parent[qRoot] = pRoot
            self.__rank[qRoot] += 1

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
            self.__parent[p] = self.__parent[self.__parent[p]]
            p = self.__parent[p]
        return p