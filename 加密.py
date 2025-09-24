#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   7jiami.py
@Time    :   2025/09/24 22:43:22
@Author  :   Li FUCHUN 
@Version :   1.0
'''


ip=input().split()
n=input()
sentancelist=[]#构建包含单词的序列
dcs=len(ip)#获得单词数
for j in range(dcs):#每个单词逐一处理
    dc=ip[j]#挑出单词
    wordlist=[]#构建包含字母的序列
    zms=len(dc)#获得字母数
    for i in range(zms):#每个字母逐一处理
        cha=dc[i]#挑出字母
        cha=(chr((int(ord(cha))-97+int(n))%26+97))#转换字母
        wordlist.append(cha)#将转换好这个的字母添加到此单词的字母序列中
    word=''.join(wordlist)#将字母序列组合成单词
    sentancelist.append(word)#将这个单词添加到此句子的单词序列中
sentance=' '.join(sentancelist)#将单词序列组合成句子
print(sentance)
