'''
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''


'''思路2：根据数组的特点，出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，因此可以最开始保存两个数值：
数组中的一个数字以及它出现的次数，然后遍历，如果下一个数字等于这个数字，那么次数加一，如果不等，次数减一，当次数
等于0的时候，在下一个数字的时候重新复制新的数字以及出现的次数置为1，直到进行到最后，然后再验证最后留下的数字是否
出现次数超过一半，因为可能前面的次数依次抵消掉，最后一个数字就直接是保留下来的数字，但是出现次数不一定超过一半。
运行时间：32ms

占用内存：5740k
'''

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 1
        number = numbers[0]
        for i in numbers[1:]:
            if number == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    number = i
                    count += 1

        times = 0            #验证数字是否正确
        for j in numbers:
            if j == number:
                times += 1

        return number if times > len(numbers) // 2 else 0