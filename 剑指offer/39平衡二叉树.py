# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 21:05
# @Author  : gaofeil

'''
题目：输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

'''
思路：方法二：自下往上 对于每个节点，都计算一下左子树
以及右子树的差的绝对值，即每个节点都判断一下。  算法复杂度O(N)
运行时间：26ms

占用内存：5732k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, p):
        return self.dfs(p) != -1
    def dfs(self, p):
        if p is None:
            return 0
        left = self.dfs(p.left)
        if left == -1:
            return -1
        right = self.dfs(p.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1