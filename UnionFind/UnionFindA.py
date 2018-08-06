#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: UnionFindA.py
@time: 2018/8/5 15:37
@desc:
"""
from DataStructure.UnionFind.UF import UF

"""
第一版并查集，本质是一个数组
"""
class UnionFindA(UF):
    def __init__(self, size):
       self.__id = [x for x in range(size)]

    def getSize(self):
        """
        :return:
        """
        return len(self.__id)

    def isConnected(self, p, q):
        """
        查找元素p和元素q是否所属一个集合
        O(1)复杂度
        :param p:
        :param q:
        :return:
        """
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        """
        合并元素p和元素q所属的集合
        O(n)复杂度
        :param p:
        :param q:
        :return:
        """
        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return
        count = len(self.__id)
        for i in range(count):
            if self.__id[i] == pID:
                self.__id[i] = qID


    def find(self, p):
        """
        查找元素p所对应的集合编号
        O(1)复杂度
        :param p:
        :return:
        """
        try:
            if p < 0 and p >= len(self.__id):
                raise Exception("p is out of bound.")
        except Exception as err:
            print(err)
            return
        return self.__id[p]
