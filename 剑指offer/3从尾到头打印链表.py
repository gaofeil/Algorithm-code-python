'''
题目：输入一个链表，从尾到头打印链表每个节点的值
'''

'''
使用insert直接在头部插入
时间 26ms
内存 6336k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        result = []
        head = listNode
        while head:
            result.insert(0, head.val)
            head = head.next
        return result
