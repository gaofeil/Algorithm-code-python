'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
最优化的方式是从左下或者右上开始搜索
从右上开始搜索，如果数组中的数比该数要大，那么想左移动一位，如果数组中的数比该数小，向下移动一位，
因为数组本身是从左到右依次增大，从上到下一次增大
'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        raw = len(array)
        col = len(array[0])    #这样写得到列

        i = 0
        j = col - 1
        while i < raw and j >= 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False
