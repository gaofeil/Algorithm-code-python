# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 21:43
# @Author  : gaofeil
'''
题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"
和"12e+4.3"都不是。
'''

'''
思路一：利用float强转
运行时间：40ms

占用内存：5712k
'''

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            return float(s)
        except:
            return 0

'''
思路二：正则表达式
运行时间：31ms

占用内存：5688k
'''

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return 0
        import re
        # 正则表达式，*匹配前一个字符出现无限次或0次，？匹配前一个字符出现一次或0次，+匹配前一个字符出现1次
        # 或无限次，.表示小数点已经转义了
        return re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$', s)
