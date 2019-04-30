'''
题目：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

'''
依旧是斐波那契数列
2*n的大矩形，和n个2*1的小矩形
其中 2*target 为大矩阵的大小
有以下几种情形：
1. n=1,  1种
2. n=2   2种
结果 f(n) = f(n-1) + f(n-2)
具体参考牛客网剑指offer本题讨论中：柠檬cold 的图解
运行时间：25ms

占用内存：5752k
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
            res = [0, 1, 2]
            while len(res) <= number:
                res.append(res[-1] + res[-2])
            return res[number]
