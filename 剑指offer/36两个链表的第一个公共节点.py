# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 20:47
# @Author  : gaofeil

'''
题目：输入两个链表，找出它们的第一个公共结点
'''

'''
思路：共同节点，意味着从共同节点开始之后所有的节点数都是相同的，这是链表，只要有一个共同节点，那么之后所有的指向
也是重复的。先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，那么我们就先让长度为m的链表走m-n个结点，然后
两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。
运行时间：28ms

占用内存：5688k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, head1, head2):
        if not head1 or not head2:
            return None

        p1, p2 = head1, head2
        length1 = length2 = 0

        while p1:
            length1 += 1
            p1 = p1.next
        while p2:
            length2 += 1
            p2 = p2.next

        if length1 > length2:
            while length1 - length2:
                head1 = head1.next
                length1 -= 1
        else:
            while length2 - length1:
                head2 = head2.next
                length2 -= 1

        while head1 and head2:
            if head1 is head2:
                return head1
            head1 = head1.next
            head2 = head2.next

        return None