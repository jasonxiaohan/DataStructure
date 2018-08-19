# -*- coding:utf-8 -*-
"""
@author daixiaohan
二分搜索树
"""
from DataStructure.LinkedListStack import LinkedListStack
from DataStructure.LinkedList import LinkedList

class BinarySearchTree:
    class Node:
        key =value = None
        # 左子树、右子树
        left = right = None

        def __init__(self, key, value):
            self.key = key
            self.value = value

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
        self.res += self.__generateDepthString(depth) + str(node.key) +"\n"

        str(self.__generateBSTString(node.left, int(depth + 1)))
        str(self.__generateBSTString(node.right, int(depth + 1)))

    def __generateDepthString(self, depth):
        re = ""
        for i in range(depth):
            re+="--"
        return re

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, key, value):
        """
        if self.root == None:
            self.root = self.Node(e)
            self.size += 1
        else:
            self.__add(self.root, e)
        """
        self.root = self.__add(self.root, key, value)
    """
   向node为根的二分搜索树中插入元素e，递归算法 
   返回插入新节点后二分搜索树的根
    """
    def __add(self, node, key, value):
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
            return self.Node(key, value)
        if key < node.key:
            node.left = self.__add(node.left, key, value)
        elif key > node.key:
            node.right = self.__add(node.right, key, value)
        return node

    """
    看二分搜索树中是否包含元素e
    """
    def contains(self, key):
        return self.__contains(self.root, key)

    """
    看以node为根的二分搜索树中是否包含元素e，递归算法
    """
    def __contains(self, node, key):
        if node == None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self.__contains(node.left, key)
        else:
            return self.__contains(node.right, key)

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
        print(node.key)
        self.__preOrder(node.left)
        self.__preOrder(node.right)

    """
    前序遍历以node为根的二分搜索树，非递归算法
    """
    def preOrderNR(self):
        stack = LinkedListStack()
        stack.push(self.root)
        while not stack.isEmpty():
            cur = stack.pop()
            print(cur.key)
            if(cur.right != None):
                stack.push(cur.right)
            if(cur.left != None):
                stack.push(cur.left)

    """
    二分搜索树的层序遍历(广度优先遍历)
    """
    def levelOrder(self):
        queue = LinkedList()
        queue.addFirst(self.root)
        while not queue.isEmpty():
            cur = queue.removeFirst()
            print(cur.key)
            if(cur.left != None):
                queue.addLast(cur.left)
            if(cur.right != None):
                queue.addLast(cur.right)

    """
    寻找二分搜索树的最小元素
    """
    def minxmum(self):
        return self.__minxmum(self.root).key

    def __minxmum(self, node):
        if(self.size == 0):
            print("BST is empty.")
            return
        if(node.left == None):
            return node
        return self.__minxmum(node.left)

    """
    寻找二分搜索树中的最大元素
    """
    def maximum(self):
        return self.__maximum(self.root).key

    def __maximum(self, node):
        if(self.size == 0):
            print("BST is empty.")
            return
        if(node.right == None):
            return node
        return self.__maximum(node.right)

    """
    从二分搜索树中删除最小值所在节点，并返回最小值
    """
    def removeMin(self):
        e = self.minxmum()
        self.root = self.__removeMin(self.root)
        return e

    def __removeMin(self, node):
        if(node.left == None):
            rightNode = node.right
            node.right = None
            self.size -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    """
    从二分搜索树中删除最大值所在的节点，并返回最大值
    """
    def removeMax(self):
        e = self.maximum()
        self.root = self.__removeMax(self.root)
        return e
    def __removeMax(self, node):
        if(node.right == None):
            leftNode = node.left
            node.left = None
            self.size -= 1
            return leftNode
        node.right = self.__removeMax(node.right)
        return node

    """
    删除元素e
    """
    def remove(self, key):
        self.root = self.__remove(self.root, key)

    def __remove(self, node, key):
        if(node == None):
            return None
        if(key < node.key):
            node.left = self.__remove(node.left, key)
            return node
        elif(key > node.key):
            node.right = self.__remove(node.right, key)
            return node
        else:
            if(node.left == None):
                nodeRight = node.right
                node.right = None
                self.size -= 1
                return nodeRight
            if(node.right == None):
                nodeLeft = node.left
                node.left = None
                self.size -= 1
                return nodeLeft
            # 否则存在左右两个子树
            successor = self.__minxmum(node.right)
            successor.right = self.__removeMin(node.right)
            successor.left = node.left
            node.left = node.right = None
            return successor



# if __name__ == '__main__':
    """
        5 
       /   \ 
      3     6 
     /  \    \ 
    2    4    8 
    """
    """
    bst = BinarySearchTree()
    # nums = [5,3,6,8,4,2]
    nums = [41, 58, 50, 42, 53, 60, 59, 63]
    for i in nums:
        bst.add(i, None)
    # bst.preOrder()
    print("")
    print(bst)
    print("")
    bst.remove(58)
    print(bst)
  
    bst.preOrderNR()
    print("")
    bst.levelOrder()
    print("")
    print(bst.minxmum())
    print("")
    print(bst.maximum())
    print("")
    print("删除最小节点："+ str(bst.removeMin()))
    print(bst)
    print("----")
    # print("删除最大节点："+ str(bst.removeMax()))
    bst.removeMax()
    print(bst)
    """
