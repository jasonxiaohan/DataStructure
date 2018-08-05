#!/usr/bin/env python
# encoding: utf-8
"""
@author: daixiaohan
@license: (C) Copyright 2018
@contact: jasonxiaohan198@qq.com
@file: UnionFindTest.py
@time: 2018/8/5 15:50
@desc:
"""
import time
import random
from DataStructure.UnionFind.UnionFindA import UnionFindA
from DataStructure.UnionFind.UnionFindB import UnionFindB
from DataStructure.UnionFind.UnionFindC import UnionFindC
from DataStructure.UnionFind.UnionFindD import UnionFindD
from DataStructure.UnionFind.UnionFindE import UnionFindE
from DataStructure.UnionFind.UnionFindF import UnionFindF

class UnionFindTest:
    @staticmethod
    def testUF(uf, m):
        size = uf.getSize()
        startTime = time.clock()
        for i in range(m):
            a = random.randrange(0, size)
            b = random.randrange(0, size)
            uf.unionElements(a, b)
        for i in range(size):
            a = random.randrange(0, size)
            b = random.randrange(0, size)
            uf.isConnected(a, b)
        endTime = time.clock()

        return endTime - startTime

if __name__ == '__main__':
    size = 1000000
    m = 1000000
    # unionA = UnionFindA(size)
    # unionB = UnionFindB(size)
    unionC = UnionFindC(size)
    unionD = UnionFindD(size)
    unionE = UnionFindE(size)
    unionF = UnionFindF(size)

    # ufa = UnionFindTest.testUF(unionA, m)
    # print("UnionFindA："+str(ufa)+" s ")
    # ufb = UnionFindTest.testUF(unionB, m)
    # print("UnionFindB："+str(ufb)+" s ")
    ufc = UnionFindTest.testUF(unionC, m)
    print("UnionFindC：" + str(ufc) + " s ")
    ufd = UnionFindTest.testUF(unionD, m)
    print("UnionFindD：" + str(ufd) + " s ")
    ufe = UnionFindTest.testUF(unionE, m)
    print("UnionFindE：" + str(ufe) + " s ")
    uff = UnionFindTest.testUF(unionF, m)
    print("UnionFindF：" + str(uff) + " s ")
