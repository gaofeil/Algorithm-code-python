# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 20:00
# @Author  : gaofeil

'''
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

'''
依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。

Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
a-b-c

运行时间：27ms
占用内存：5728k
'''

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)   #list() 方法用于将元组转换为列表。

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            #切片 假设abc输入，当i为0是，第一个join为空，第二个join为bc
            #在下面的for循环，j取值为bc
            for j in temp:
                pStr.append(charList[i]+j)
        return pStr