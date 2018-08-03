# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 11:24
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : MapSum.py
# @Software: PyCharm

"""
解决leetcode中的677号问题
"""
class MapSum:
    class Node:
        next = {}
        value = 0
        def __init__(self, value=0):
            self.value = value
            self.next = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        cur = self.root
        for w in key:
            if cur.next.get(w) == None:
                cur.next[w] = self.Node()
            cur = cur.next.get(w)
        cur.value = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for w in prefix:
            if cur.next.get(w) == None:
                return 0
            cur = cur.next.get(w)
        return self.__sum(cur)

    def __sum(self, node):
        res = node.value
        keys = node.next.keys()
        for w in keys:
            res += int(self.__sum(node.next.get(w)))
        return res

if __name__ == '__main__':
    mapSum = MapSum()
    mapSum.insert("apple", 3)
    print(mapSum.sum("ap"))
    mapSum.insert("app", 2)
    print(mapSum.sum("ap"))
