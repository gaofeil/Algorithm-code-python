# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 20:41
# @Author  : gaofeil
'''
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组
中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
'''

'''
notes：这一题没法用python做，用python始终是超时的
思路一：很巧妙
在牛客网上运算超时，但是思想很好 用空间换时间

过程：
输入数组：data=[3,2,1,5,4,6,0,7]
排序好数组：dataSorted=[0,1,2,3,4,5,6,7]
顺序遍历dataSorted数组，第一个元素0是最小的元素，因此在data数组中，
0前面有多少个数，就有多少个逆序对。在0检测完之后，将0从data数组中删除，
data=[3,2,1,5,4,6,7]，dataSorted数组遍历到1，而1其实就是[1,2,3,4,5,6,7]中的最小元素
因此，原问题就变为子问题：
输入数组：data=[3,2,1,5,4,6,7]
排序好数组：dataSorted=[1,2,3,4,5,6,7]  ……直到遍历到最后一个元素。

该方法复杂度分析：
sort排序复杂度为O(nlogn)；单次index查找复杂度为O(lgn)，要查找n次，
复杂度也为O(nlogn)；单次remove操作中：查找该数的复杂度为O(lgn)，移动该数后面的数复杂度为O(n)，
因此复杂度为O(n)，要remove操作n次，复杂度为O(n^2)；因此总的复杂度为O(n^2)。

'''

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        copy = []
        count = 0
        for i in data:
            copy.append(i)
        copy.sort()

        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])

        return count % 10000000007

'''
思路二：这一题核心还是要用归并排序，归并排序能够有效的减少最坏时间复杂度，但是它有额外的开销，以空间换时间
归并排序，就是把原数据分成两个数组，每次取两个数组中的最小值放入一个新的数组中，直到其中一个数组全部取完
不过还是超时
'''

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        length = len(data)
        if data == None or length <= 0:
            return 0
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]

        count = self.InversePairsCore(data, copy, 0, length - 1)
        return count % 10000000007

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end

        indexCopy = end
        count = 0
        # 对两个数组进行对比取值的过程
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        # 剩下的一个数组未取完的操作
        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start + length + 1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count
