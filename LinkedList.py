# -*- coding:utf-8 *-*
"""
链表
"""
class LinkedList:
    # 节点设计成内部类
    class __Node:
        e = None
        next = None

        def __init__(self, e, next=None):
            self.e = e
            self.next = next

        def __str__(self):
            return str(self.e)

    __dummyHead = None
    __size = 0

    def __init__(self):
        self.__dummyHead = self.__Node(None, None)
        self.__size = 0

    """
    获取链表中的元素个数
    """
    def getSize(self):
        return self.__size

    """
    返回链表是否为空
    """
    def isEmpty(self):
        return self.__size == 0

    """
    在链表index(0-based)位置添加新的元素e
    """
    def add(self, index, e):
        if index < 0 or index > self.__size:
            print("Add failed.Illegal index.")
            return

        prev = self.__dummyHead
        for i in range(int(index)):
            prev = prev.next

        # node = self.__Node(e)
        # node.next = prev.next
        # prev.next = node

        prev.next = self.__Node(e, prev.next)
        self.__size += 1

    """
        在链表头添加元素e
        """

    def addFirst(self, e):
        self.add(0, e)

    """
    在链表末尾添加新的元素e
    """
    def addLast(self, e):
        self.add(self.__size, e)

    """
    获得链表的第index(0-based)个位置的元素
    """
    def get(self, index):
        if index < 0 or index > self.__size:
            print("Get failed.Illegal index.")
            return
        cur = self.__dummyHead.next
        for i in range(int(index)):
            cur = cur.next
        return cur.e

    """
    获取链表的第一个元素
    """
    def getFirst(self):
        return self.get(0)

    """
    获取链表的最后一个元素
    """
    def getLast(self):
        return self.get(int(self.__size-1))

    """
    修改链表的第index(0-based)位置的元素e
    """
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            print("Set failed.Illegal index.")
            return
        cur = self.__dummyHead.next
        for i in range(int(index)):
            cur = cur.next
        cur.e = e

    """
    查找链表中是否有元素e
    """
    def contains(self, e):
        cur = self.__dummyHead.next
        while cur != None:
            try:
                if str(cur.e) == str(e):
                    return True
                cur = cur.next
            except Exception as e:
                return False
        return False

    def __str__(self):
        res = ""
        cur = self.__dummyHead.next
        while cur != None:
            res += str(cur)+ "->"
            cur = cur.next
        res += "NULL"
        return res

if __name__ == '__main__':
    linkedList = LinkedList()
    for i in range(5):
        linkedList.addFirst(i)
        print(linkedList)
    linkedList.add(2, 666)
    print(linkedList)

    print(linkedList.contains(6666))