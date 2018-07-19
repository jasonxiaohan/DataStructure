# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 15:29
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : TestUnit.py
# @Software: PyCharm

from DataStructure.BST.BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    """
             5 
           /   \ 
          3     6 
         /  \    \ 
        2    4    8 
        """
    bst = BinarySearchTree()
    # nums = [5,3,6,8,4,2]
    nums = [41, 58, 50, 42, 53, 60, 59, 63]
    for i in nums:
        bst.add(i)
    # bst.preOrder()
    print("")
    print(bst)
    print("")
    bst.remove(58)
    print(bst)
    """
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
