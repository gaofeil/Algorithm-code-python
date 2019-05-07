# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 19:39
# @Author  : gaofeil
'''
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
如果输入如下矩阵： 1  2  3  4
                   5  6  7  8
                   9 10 11 12
                  13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
'''
最佳思路：：：
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可
运行时间：22ms
占用内存：5744k
'''
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while (matrix):
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        newmat = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col):    #双层for循环，每次外循环不动，内循环走一遍
            newmat1 = []
            for j in range(row):
                newmat1.append(matrix[j][i])
            newmat.append(newmat1)
        newmat.reverse()         #得到[6,9],[5,8],[4,7]
        return newmat

'''
相同思路一行表示
28 ms	5716K
'''

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        return matrix and list(matrix.pop(0)) + self.printMatrix(zip(*matrix)[::-1])