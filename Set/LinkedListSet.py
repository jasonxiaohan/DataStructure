# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 18:28
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : LinkedListSet.py
# @Software: PyCharm

from DataStructure.Set.Set import Set
from DataStructure.LinkedList import LinkedList

"""
使用链表完成SET的底层实现
"""
class LinkedListSet(Set):
    def __init__(self):
        self.link = LinkedList()

    def add(self, e):
        if(self.link.contains(e) != True):
            self.link.addFirst(e)

    def remove(self, e):
       self.link.removeElement(e)

    def contains(self, e):
        return self.link.contains(e)

    def getSize(self):
        return self.link.getSize()

    def isEmpty(self):
        return self.link.isEmpty()
