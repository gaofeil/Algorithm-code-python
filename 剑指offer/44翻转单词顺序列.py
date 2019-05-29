# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 21:11
# @Author  : gaofeil
'''
题目：牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容
颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把
句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s == None or len(s) <= 0:
            return ''
        # 以空格为界，提取单一字符，然后用切片拍一下顺序
        return ' '.join(s.split(' ')[::-1])

'''
line[:-1]其实就是去除了这行文本的最后一个字符（换行符）后剩下的部分。
line = "abcde"line[:-1]结果为：'abcd'
line = "abcde"line[::-1]结果为：'edcba'
'''