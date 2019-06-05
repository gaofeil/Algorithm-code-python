# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 21:21
# @Author  : gaofeil
'''
题目：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

'''
思路一：用sum函数，但是特别注意sum()求和里面是个[]列表对象，直接输入num，num2是不行的
运行时间：39ms

占用内存：5752k
'''

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        return sum([num1,num2])

'''
思路二：
 两个数异或：相当于每一位相加，而不考虑进位；
 两个数相与，并左移一位：相当于求得进位；
 将上述两步的结果相加，即重复上述两个步骤，直到不产生进位为止
超时了
'''

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            # 异或运算相当于只求和不进位
            sum = num1 ^ num2
            # 与操作，并向左移一位，相当于求进位
            carray = (num1 & num2) << 1
            num1 = sum
            num2 = carray
        return num1