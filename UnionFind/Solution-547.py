# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 10:09
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : Solution-547.py
# @Software: PyCharm
from DataStructure.UnionFind.UnionFindF import UnionFindF

"""
Leetcode 547. Friend Circles
"""
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        uf = UnionFindF(n)
        for i in range(n):
            for j in range(i):
                if M[i][j] == 1:
                    uf.unionElements(i, j)
        s = set()
        for i in range(n):
            s.add(uf.find(i))
        return len(s)

if __name__ == '__main__':
    solution = Solution()
    M = [[1,1,0], [1,1,0], [0,0,1]]
    print(solution.findCircleNum(M))