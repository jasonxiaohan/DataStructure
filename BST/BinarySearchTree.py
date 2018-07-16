# -*- coding:utf-8 -*-
"""
@author daixiaohan
二分搜索树
"""

from DataStructure.LinkedListStack import LinkedListStack

class BinarySearchTree:
    class Node:
        e = None
        left = right = None

        def __init__(self, e):
            self.e = e

    root = None
    size = 0
    res = ""

    def __init__(self):
        self.size = 0

    def __str__(self):
        str(self.__generateBSTString(self.root, 0))
        return self.res

    """
    生成以node为根节点，深度为depth的描述二叉树的字符串
    """
    def __generateBSTString(self, node, depth):
        if node == None:
            self.res += self.__generateDepthString(depth)+"null\n"
            return
        self.res += self.__generateDepthString(depth) + str(node.e) +"\n"

        str(self.__generateBSTString(node.left, int(depth + 1)))
        str(self.__generateBSTString(node.right, int(depth + 1)))

    def __generateDepthString(self, depth):
        re = ""
        for i in range(depth):
            re+="--"
        return re

    def geSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, e):
        """
        if self.root == None:
            self.root = self.Node(e)
            self.size += 1
        else:
            self.__add(self.root, e)
        """
        self.root = self.__add(self.root, e)
    """
   向node为根的二分搜索树中插入元素e，递归算法 
   返回插入新节点后二分搜索树的根
    """
    def __add(self, node, e):
        """
        if node.e == e:
            return
        else:
            if e < node.e and node.left == None:
                node.left = self.Node(e)
                self.size += 1
                return
            elif e > node.e and node.right == None:
                node.right = self.Node(e)
                self.size += 1
                return
        """
        if node == None:
            self.size += 1
            return self.Node(e)
        if e < node.e:
            node.left = self.__add(node.left, e)
        elif e> node.e:
            node.right = self.__add(node.right, e)
        return node

    """
    看二分搜索树中是否包含元素e
    """
    def contains(self, e):
        return self.__contains(self.root, e)

    """
    看以node为根的二分搜索树中是否包含元素e，递归算法
    """
    def __contains(self, node, e):
        if node == None:
            return False
        if node.e == e:
            return True
        elif e < node.e:
            return self.__contains(node.left, e)
        else:
            return self.__contains(node.right, e)

    """
    二分搜索树的前序遍历
    """
    def preOrder(self):
        self.__preOrder(self.root)

    """
    前序遍历以node为根的二分搜索树，递归算法
    """
    def __preOrder(self, node):
        if node == None:
            return
        print(node.e)
        self.__preOrder(node.left)
        self.__preOrder(node.right)

    """
    二分搜索树的非递归前序遍历
    """
    def preOrderNR(self):
        stack = LinkedListStack()
        stack.push(self.root)
        while stack.isEmpty() != None:
            cur = stack.pop()
            if(cur == None):
                break
            print(str(cur.e))
            if(cur.right != None):
                stack.push(cur.right)
            if(cur.left != None):
                stack.push(cur.left)

if __name__ == '__main__':
    bst = BinarySearchTree()
    nums = [5,3,6,8,4,2]
    for i in nums:
        bst.add(i)
    bst.preOrder()
    print("")
    bst.preOrderNR()