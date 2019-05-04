'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

'''
方法一：   使用数组
运行时间：43ms
占用内存：5728k

'''
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd, even = [], []
        for i in array:
            odd.append(i) if i % 2 == 1 else even.append(i)
        return odd + even


'''
方法二： 使用lambda表达式 
运行时间：25ms
占用内存：5732k
'''
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
         return sorted(array,key=lambda c:c%2,reverse=True)
'''sorted  高阶函数 用于排序   
    lambda 匿名函数 
    举例说明  lambda x:x*x
    就是： def f(x):
                return x*x   具体参考廖雪峰python教程 函数式编程-匿名函数

'''