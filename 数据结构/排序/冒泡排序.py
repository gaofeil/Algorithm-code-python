# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 21:47
# @Author  : gaofeil
'''

'''
'''
在循环中定义了一个变量count，如果第一次循环后count没有变化，就说明输入的是有序序列
这时我们直接return退出循环，这时候的时间复杂度为O(n)
扩展知识：冒泡排序还是一种稳定性的算法，如果序列中出现两个相同的值的时候，
无论选取最大值，还是最小值进行排序，最后两个相同值的前后位置都是不变的。

实现思路： 使用双重for循环，内层变量为i， 外层为j，
在内层循环中不断的比较相邻的两个值（i, i+1）的大小，如果i+1的值大于i的值，交换两者位置，
每循环一次，外层的j增加1，等到j等于n-1的时候，结束循环

第一次循环： j = 0, i~n-2 range(0, n-1)
第二次循环： j = 1, i~n-3 range(0, n-1-1)
第三次循环： j = 2, i~n-4 range(0, n-1-1-1)
—> range(0, n-1-j)
'''

def bubble_sort(arr):
    for j in range(len(arr)-1, 0, -1):
        count = 0
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
        if count == 0:
            return

arr = [7, 4, 3, 67, 34, 1, 8]
bubble_sort(arr)
print(arr)  # [1, 3, 4, 7, 8, 34, 67]
