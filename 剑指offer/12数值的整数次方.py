'''
题目：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
'''

'''
方法：
需要注意的地方:
当指数为负数的时候
当底数为零切指数为负数的情况
在判断底数base是不是等于0的时候,不能直接写base==0, 因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内

当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
c++中的小技巧：：利用右移一位运算代替除以2
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
优化代码速度

运行时间：30ms

占用内存：5868k
'''

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base**exponent






