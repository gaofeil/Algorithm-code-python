'''
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

'''
 使用replace
时间 25ms
内存 5624k
'''
class Solution:
    # s 原字符串
    def replaceSpace(self, s):
        return s.replace(' ','%20')
