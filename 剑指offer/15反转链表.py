'''
题目：输入一个链表，反转链表后，输出新链表的表头。
'''

'''
python的非递归实现。思路很简单：1->2->3->4->5，遍历链表，把1的next置为None，
2的next置为1，以此类推，5的next置为4。得到反转链表。需要考虑链表只有1个元素的情况。
图中有具体的每步迭代的思路，最后输出pre而不是cur是因为最后一次迭代后cur已经指向None了，
而pre是完整的反向链表
简而言之：：：
链表的翻转，例如 1->2->3->4->5  ==>  5->4->3->2->1

运行时间：26ms

占用内存：5708k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pre = None
        while pHead:
            tmp = pHead.next   #把当前节点的下一个节点保存下来
            pHead.next = pre   #把前一个节点移到当前节点的下一个节点，因为要翻转节点，pre始终指向要反转节点的首节点
            pre = pHead        #当前节点向后移一位
            pHead = tmp        #把之前保存的下一个节点指针再给当前节点接着翻转
        return pre


    #可参考牛客网讨论  瑞博远航的解释