# -*- coding:utf-8 -*-
from DataStructure.ListNode import ListNode

class Solution:

    """
    leetcode：19
    删除链表中的倒数第N个节点
    """
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(None, None)
        dummyHead.next = head

        prev = dummyHead
        size = 0
        while prev.next != None:
            prev.next = prev.next.next
            size += 1

        dummyHead.next = head
        prev = dummyHead

        count =0
        while prev.next != None:
            if count == int(size-n):
                prev.next = prev.next.next
            else:
                prev = prev.next
            count += 1
        return dummyHead.next


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4,5]
    head = ListNode(None, nums)

    print(solution.removeNthFromEnd(head, 1))