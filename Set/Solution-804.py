# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 15:57
# @Author  : daixiaohan
# @Email   : jasonxiaohan198@qq.com
# @File    : Solution-804.py
# @Software: PyCharm

"""
解决leetcode中804号问题
"""
class Solution:
    def uniqueMorseRepresentations(self, words):
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        se = set()
        for word in words:
            res = ""
            for w in word:
                res +=codes[ord(w) - ord('a')]
            se.add(res)
        return len(se)

if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    solution = Solution()
    solution.uniqueMorseRepresentations(words)