#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   7jiami.py
@Time    :   2025/09/24 22:43:22
@Author  :   Li FUCHUN 
@Version :   4.0
'''


ip=input('请输入原文').split()
n=input('请输入密钥')
sentancelist=[]#构建包含单词的序列
wordnum=len(ip)#获得单词数
nlist=[]
nnum=len(n)
for k in range (nnum):
    chaa=ord(n[0])
    if chaa>=48 and chaa<=57:
        chaa=str(chaa-48)
    else :
        chaa=str(chaa)
    nlist.append(chaa)
n=''.join(nlist)
for j in range(wordnum):#每个单词逐一处理
    word=ip[j]#挑出单词
    wordlist=[]#构建包含字母的序列
    chanum=len(word)#获得字母数
    for i in range(chanum):#每个字母逐一处理
        cha=word[i]#挑出字母
        if ord(cha)>=97 and ord(cha)<=122:
            chanew=(chr((int(ord(cha))-97+int(n))%26+97))#转换字母（小写）
        elif ord(cha)>=65 and ord(cha)<=90:
            chanew=(chr((int(ord(cha))-65+int(n))%26+65))#转换字母（大写）
        else :
            chanew=(chr((int(ord(cha))+160+int(n)%900)))#其他
        wordlist.append(chanew)#将转换好这个的字母添加到此单词的字母序列中
    word=''.join(wordlist)#将字母序列组合成单词
    sentancelist.append(word)#将这个单词添加到此句子的单词序列中
sentance=' '.join(sentancelist)#将单词序列组合成句子
print(sentance)
