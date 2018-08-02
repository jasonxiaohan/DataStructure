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

    def isPrefix(self, prefix):
        """
        查询是否在Trie中有单词以prefix为前缀
        :param prefix:
        :return:
        """
        cur = self.root
        for w in prefix:
            if cur.next.get(w) == None:
                return False
            cur = cur.next.get(w)
        return True

    def search(self, word):
        """
        leetcode：211题号
        以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母
        :param word:
        :return:
        """
        return self.__match(self.root, word, 0)

    def __match(self, node, word, index):
        """
        正则匹配word
        :param node:
        :param word:
        :param index:
        :return:
        """
        if index == len(word):
            return node.isWord
        c = word[index]
        if c != '.':
            if node.next.get(c) == None:
                return False
            return self.__match(node.next.get(c), word, int(index+1))
        else:
            list = node.next.keys()
            for w in list:
                if self.__match(node.next.get(w), word, int(index+1)):
                    return True
            return False

"""
if __name__ == '__main__':
    trie = Trie()
    trie.add("bad")
    trie.add("dad")
    trie.add("mad")
    print(trie.search("pad"))
    print(trie.search("dad"))
    print(trie.search(".ad"))
    print(trie.search("b.."))
"""