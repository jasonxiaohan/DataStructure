# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 17:56
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : Trie.py
# @Software: PyCharm

"""
Trie字典树
"""
class Trie:
    class Node:
        isWord = False
        next = {}
        def __init__(self, isWord=False):
            self.isWord = isWord
            self.next = {}

    def __init__(self):
        self.root = self.Node()
        self.size = 0

    def getSize(self):
        """
        获得Trie中存储的单词数量
        :return:
        """
        return self.size

    def add(self, word):
        """
        向字典树中添加单词word
        :param word:
        :return:
        """
        cur = self.root
        for w in word:
            if cur.next.get(w) == None:
                cur.next[w] = self.Node()
            cur = cur.next.get(w)
        if cur.isWord == False:
            cur.isWord = True
            self.size += 1

    def contains(self, word):
        """
        查询单词中是否在Trie中
        :param word:
        :return:
        """
        cur = self.root
        for w in word:
            if cur.next.get(w) == None:
                return False
            cur = cur.next.get(w)
        return cur.isWord

