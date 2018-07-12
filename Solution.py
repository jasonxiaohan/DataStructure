# -*- coding:utf8 -*-
from DataStructure.ArrayStack import ArrayStack

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    """
    20. 有效的括号
    """
    def isValid(self, s):
        # stack = []
        stack = ArrayStack()
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
               stack.push(s[i])
            else:
                if stack.getSize() == 0:
                    return False
                topChar = stack.pop()
                if s[i] == ')' and topChar != '(':
                    return False
                if s[i] == ']' and topChar !='[':
                    return False
                if s[i] == '}' and topChar !='{':
                    return False
        if stack.getSize() > 0:
            return False
        return True

    """
       496
       下一个更大元素
       """

    def nextGreaterElement(self, findNums, nums):
        data = []
        for fnum in findNums:
            for num in nums:
                if fnum == num and nums.index(num) + 1 < len(nums):
                    stack = nums[nums.index(num) + 1:]
                    bFind = False
                    for m in stack:
                        if m > fnum and not bFind:
                            data.append(m)
                            bFind = True
                    if not bFind:
                        data.append(-1)
                elif fnum == num:
                    data.append(-1)
        return data

    """
    leetcode:316
    去除重复字母
    """
    def removeDuplicateLetters(self, s):
        scount = {}
        # 标记是否访问过
        visited = []
        for i in range(len(s)):
            if s[i] in scount:
                scount[s[i]] +=1
            else:
                scount[s[i]] = 1
        res = []
        for i in range(len(s)):
            # 每次遍历一次字符就将它出现的次数减1
            # 如果结果字符串尾端的字符比将要插入字符大，而且后面字符串中还有这个字符，就弹出
            scount[s[i]]-=1
            if s[i] in visited[s[i]]:
                continue
            if len(res) > 0 and str(s[i]) < str(res[len(res) -1]) and scount[s[i]] > 0:
                res.pop()
            res.append(s[i])
            visited.append(s[i])
        return res

    """
    203 
    删除链表中等于给定值 val 的所有节点。
    """
    def removeElements1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None and head.val == val:
            """
            delNode = head
            head = head.next
            delNode.next = None
            """
            head = head.next
        if head == None:
            return None
        prev = head
        while prev.next != None:
            if prev.next.val == val:
                """
                delNode = prev.next
                prev.next = delNode.next
                delNode.next = None
              """
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head

    """
    203 
    删除链表中等于给定值 val 的所有节点
    使用虚拟头节点
    """
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(-1)
        dummyHead.next = head

        prev = dummyHead
        while prev.next != None:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummyHead.next

if __name__ == '__main__':
    solution = Solution()
    listNode = ListNode(1)
    print(listNode)
    res = solution.removeElements(listNode, 6)
    print(res)
# if _name__ == '__main__':
    # solution = Solution()
    """
    20. 有效的括号
    """
    # isvalid = solution.isValid('{[]}()')
    # print(isvalid)

    # data = solution.removeDuplicateLetters("cbacdcbc")
    # print(data)