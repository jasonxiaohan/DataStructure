# -*- coding:utf-8 -*-
from DataStructure.ListNode import ListNode

class Solution:
    def removeElements(self, head, val):
        if head == None:
            return None
        """
        res = self.removeElements(head.next, val)
        if head.val == val:
            return res
        else:
            head.next = res;
            return head
        """

        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,6,3,4,5,6]
    head = ListNode(None, nums)
    print(head)
    res = solution.removeElements(head, 6)
    print(res)