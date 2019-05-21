# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 19:36
# @Author  : gaofeil

'''
题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印
'''

'''
实际就是广度优先搜索 BFS, 借助一个队列就可以实现
先根节点入队，然后：
1.从队列中取出一个元素
2.访问该元素所指的结点
3.若该元素所指结点的左、右孩子结点非空，则将其左、右孩子的指针顺序入队
利用队列，首先将根节点放入队列中，取队列的首节点，把值存进列表，
然后考虑左右指针，把指针放进列表，再存值
运行时间：25ms

占用内存：5752k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

''' 方法一样
运行时间：26ms

占用内存：5736k'''
def PrintFromTopToBottom(self, root):
        if not root:
            return []
        currentStack = [root]
        res = []
        while currentStack:
            nextStack = []
            for i in currentStack:
                if i.left: nextStack.append(i.left)
                if i.right: nextStack.append(i.right)
                res.append(i.val)
            currentStack = nextStack
        return res