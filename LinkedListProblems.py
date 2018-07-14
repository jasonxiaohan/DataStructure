# -*- coding:utf-8 -*-
from DataStructure.ListNode import ListNode

"""
LinkedListProblems.pdf
"""
class LinkedListProblems:
    """
     Given a list and an int, return the number of times that int occurs
     in the list.
    """
    def Count(self, head, searchFor):
        dummpyHead = ListNode(None, None)
        dummpyHead.next = head
        prev = dummpyHead
        count = 0
        while prev.next != None:
            if prev.next.val == searchFor:
                count += 1
            prev = prev.next
        return count

    """
     Given a list and an index, return the data
     in the nth node of the list. The nodes are numbered from 0.
     Assert fails if the index is invalid (outside 0..lengh-1).
    """
    def GetNth(self, head, index):
        count = 0
        dummpyHead = ListNode(None, None)
        dummpyHead.next = head

        prev = dummpyHead
        while prev.next != None:
            if count == index:
                return prev.next.val
            prev = prev.next
            count += 1
        return None

if __name__ == '__main__':
    linkedList = LinkedListProblems()
    nums = [1,2,3,1]
    head = ListNode(None, nums)
    count = linkedList.Count(head, 2)
    print(count)

    value = linkedList.GetNth(head, 2)
    print(value)


