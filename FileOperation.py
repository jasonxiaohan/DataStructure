# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 11:18
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : FileOperation.py
# @Software: PyCharm
import jieba
"""
文件操作相关类
"""
class FileOperation:
    """
    读取文件名称为filename文件中的名称，并将读取的单词放到列表中
    """
    @staticmethod
    def readFile(filename):
        words = []
        if(filename == None):
            print("filename is null")
            return False
        with open(filename, encoding='UTF-8-sig') as f:
            seg_list = jieba.cut(f.read())
            for tk in seg_list:
                if(tk.strip() != "" and tk.strip() not in ['.',',',';',':','\'']):
                    words.append(tk.strip())
        return words



