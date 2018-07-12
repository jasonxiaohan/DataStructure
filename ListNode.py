# -*- coding:utf-8 -*-
"""
leetcode 203
删除链表中的节点
构造ListNode链表节点数据
"""
class ListNode(object):
    val = None
    next = None
    def __init__(self, x = None, arr = None):
        if arr != None and len(arr) > 0:
            self.val = arr[0]
            cur = self
            for i in range(1, len(arr)):
                cur.next = ListNode(arr[i], None)
                cur = cur.next
        elif x != None:
            self.val = x
            self.next = None

    def __str__(self):
        res = ""
        cur = self
        while cur != None:
            res += str(cur.val) + "->"
            cur = cur.next;
        res+="NULL"
        return res
