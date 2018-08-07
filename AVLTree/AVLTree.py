# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 18:26
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : AVLTree.py
# @Software: PyCharm

from DataStructure.FileOperation import FileOperation
from DataStructure.Map.Map import Map

"""
使用二分搜索树实现map
"""
class AVLTree(Map):
    class Node:
        key = None
        value = None
        # 左子树、右子树
        left = right = None

        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.height = 1

    root = None
    size = 0
    res = ""

    def __init__(self):
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def isBST(self):
        """
        判断该二叉树是否是一颗二分搜索树
        :return:
        """
        keys = []
        self.__inOrder(self.root, keys)

        length = len(keys)
        for i in range(1,length):
            if keys[i-1] > keys[i]:
                return False
        return True

    def __inOrder(self, node, keys):
        """
        中序遍历
        :param keys:
        :return:
        """
        if node == None:
            return
        self.__inOrder(node.left, keys)
        keys.append(node.key)
        self.__inOrder(node.right, keys)

    def isBalanced(self):
        """
        判断该二叉树是否是一颗平衡二叉树
        :return:
        """
        return self.__isBalanced(self.root)

    def __isBalanced(self, node):
        """
        判断以Node为根的二叉树是否是一颗平衡二叉树，递归算法
        :param node:
        :return:
        """
        if node == None:
            return True
        balanceFactor = self.__getBalanceFactor(node)
        if abs(balanceFactor) > 1:
            return False
        return self.__isBalanced(node.left) and self.__isBalanced(node.right)

    def __getHeight(self, node):
        """
        获取节点node的高度
        :param node:
        :return:
        """
        if node == None:
            return 0
        return node.height

    def __getBalanceFactor(self, node):
        """
        获取节点node的平衡因子
        :param node:
        :return:
        """
        if node == None:
            return 0
        return  int(self.__getHeight(node.left) - self.__getHeight(node.right))

    def add(self, key, value):
        self.root = self.__add(self.root, key, value)

    def __add(self, node, key, value):
        """
        向node为根的二分搜索树中插入元素(k,v)，递归算法
       返回插入新节点后二分搜索树的根
        :param node:
        :param key:
        :param value:
        :return:
        """
        if node == None:
            self.size += 1
            return self.Node(key, value)
        if key < node.key:
            node.left = self.__add(node.left, key, value)
        elif key > node.key:
            node.right = self.__add(node.right, key, value)
        else: # key==node.key
            node.value = value
        # 更新height值
        node.height = 1 + int(max(self.__getHeight(node.right), self.__getHeight(node.left)))
        # 计算平衡因子
        balanceFactor = self.__getBalanceFactor(node)
        # if abs(balanceFactor) > 1:
        #     print("unbalanced："+str(balanceFactor))
        # 平衡维护
        # LL
        if balanceFactor > 1 and self.__getBalanceFactor(node.left) >= 0:
            return self.__rightRotate(node)
        # RR
        if balanceFactor < -1 and self.__getBalanceFactor(node.right) <= 0:
            return self.__leftRotate(node)
        # LR
        if balanceFactor > 1 and self.__getBalanceFactor(node.left) < 0:
            node.left = self.__leftRotate(node.left)
            return self.__rightRotate(node)
        # RL
        if balanceFactor < - 1 and self.__getBalanceFactor(node.right) > 0:
            node.right = self.__rightRotate(node.right)
            return self.__leftRotate(node)
        return node

    def __rightRotate(self, y):
        """
        对节点nodeY进行向右旋转操作，返回旋转后新的根节点x
           y                              x
          / \                           /   \
          x   T4     向右旋转 (y)        z     y
         / \       - - - - - - - ->    / \   / \
        z   T3                       T1  T2 T3 T4
       / \
     T1   T2
        :param y:
        :return:
        """
        x = y.left
        T3 = x.right
        # 向右旋转
        x.right = y
        y.left = T3
        # 更新height值
        y.height = max(self.__getHeight(y.left), self.__getHeight(y.right)) + 1
        x.height = max(self.__getHeight(x.left), self.__getHeight(x.right)) + 1
        return x

    def __leftRotate(self, y):
        """
        // 对节点y进行向左旋转操作，返回旋转后新的根节点x
    //    y                             x
    //  /  \                          /   \
    // T1   x      向左旋转 (y)       y     z
    //     / \   - - - - - - - ->   / \   / \
    //   T2  z                     T1 T2 T3 T4
    //      / \
    //     T3 T4
        :param x:
        :return:
        """
        x = y.right
        T2 = x.left
        # 向左旋转过程
        x.left = y
        y.right = T2
        y.height = max(self.__getHeight(y.left), self.__getHeight(y.right)) + 1
        x.height = max(self.__getHeight(x.left), self.__getHeight(x.right)) + 1
        return x


    # 返回以node为根节点的二分搜索树，key所在的节点
    def __getNode(self, node, key):
        if(node == None):
            return None
        if(key == node.key):
            return node
        if(key < node.key):
            return self.__getNode(node.left, key)
        else:
            return self.__getNode(node.right, key)

    def contains(self, key):
        return self.__getNode(self.root, key) != None

    def get(self, key):
        node = self.__getNode(self.root, key)
        return node.value if node != None else None

    def set(self, key, value):
        node = self.__getNode(self.root, key)
        if(node == None):
            print(str(key)+" doesn't exist!")
            return
        node.value = value

    """
    寻找二分搜索树的最小元素
    """
    def minxmum(self):
        return self.__minxmum(self.root).key

    def __minxmum(self, node):
        if (self.size == 0):
            print("BST is empty.")
            return
        if (node.left == None):
            return node
        return self.__minxmum(node.left)

    """
   从二分搜索树中删除最小值所在节点，并返回最小值
   """
    def removeMin(self):
        e = self.minxmum()
        self.root = self.__removeMin(self.root)
        return e

    def __removeMin(self, node):
        if (node.left == None):
            rightNode = node.right
            node.right = None
            self.size -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    """
    删除元素e
    """
    def remove(self, key):
        node = self.__getNode(self.root, key)
        if(node != None):
            self.root = self.__remove(self.root, key)
            return node
        return None

    def __remove(self, node, key):
        if (node == None):
            return None
        if (key < node.key):
            node.left = self.__remove(node.left, key)
            retNode = node
        elif (key > node.key):
            node.right = self.__remove(node.right, key)
            retNode = node
        else:
            if (node.left == None):
                nodeRight = node.right
                node.right = None
                self.size -= 1
                retNode = nodeRight
            elif (node.right == None):
                nodeLeft = node.left
                node.left = None
                self.size -= 1
                retNode = nodeLeft
            else:
                # 待删除节点左右字数均不为空的情况
                # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
                # 用这个节点顶替待删除节点的位置
                successor = self.__minxmum(node.right)
                successor.right = self.__remove(node.right, successor.key)
                successor.left = node.left
                node.left = node.right = None
                retNode = successor
        if retNode == None:
            return None

        # 更新height值
        retNode.height = 1 + int(max(self.__getHeight(retNode.right), self.__getHeight(retNode.left)))
        # 计算平衡因子
        balanceFactor = self.__getBalanceFactor(retNode)

        # 平衡维护
        # LL
        if balanceFactor > 1 and self.__getBalanceFactor(retNode.left) >= 0:
            return self.__rightRotate(retNode)
        # RR
        if balanceFactor < -1 and self.__getBalanceFactor(retNode.right) <= 0:
            return self.__leftRotate(retNode)
        # LR
        if balanceFactor > 1 and self.__getBalanceFactor(retNode.left) < 0:
            retNode.left = self.__leftRotate(retNode.left)
            return self.__rightRotate(retNode)
        # RL
        if balanceFactor < - 1 and self.__getBalanceFactor(retNode.right) > 0:
            retNode.right = self.__rightRotate(retNode.right)
            return self.__leftRotate(retNode)
        return retNode

if __name__ == '__main__':
    filename = '../pride-and-prejudice.txt'
    words = FileOperation.readFile(filename)
    print(len(words))
    avl = AVLTree()
    for word in words:
        if(avl.contains(word)):
            avl.set(word, int(avl.get(word))+1)
        else:
            avl.add(word, 1)
    print("Total different words："+str(avl.getSize()))
    print("Frequency of PRIDE："+str(avl.get("pride")))
    print("Frequency of PREJUDICE："+str(avl.get("prejudice")))

    print("is BST："+ str(avl.isBST()))
    print("is Balanced："+ str(avl.isBalanced()))
