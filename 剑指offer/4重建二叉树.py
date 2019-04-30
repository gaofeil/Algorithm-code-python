'''
题目：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

'''
1.先求出根节点（前序序列第一个元素）。
2.将根节点带入到中序遍历序列中求出左右子树的中序遍历序列。
3.通过左右子树的中序序列元素集合带入前序遍历序列可以求出左右子树的前序序列。
4.左右子树的前序序列第一个元素分别是根节点的左右儿子
5.求出了左右子树的4种序列可以递归上述步骤
46ms
5760k
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:val + 1], tin[:val])
        root.right = self.reConstructBinaryTree(pre[val + 1:], tin[val + 1:])
        return root
