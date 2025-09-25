#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   解密.py
@Time    :   2025/09/25 17:29:07
@Author  :   Li FUCHUN 
@Version :   1.0
'''

ip=input().split()
n=input()
sentancelist=[]
wordnum=len(ip)
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
for j in range (wordnum):
    word=ip[j]
    wordlist=[]
    chanum=len(word)
    for i in range(chanum):
        cha=word[i]
        if ord(cha)>=97 and ord(cha)<=122:
            chanew=chr((ord(cha)-71-int(n)%26)%26+97)
        elif ord(cha)>=65 and ord(cha)<=91:
            chanew=chr((ord(cha)-39-int(n)%26)%26+65)
        else :
            chanew=chr(ord(cha)-int(n)%900-160)
        wordlist.append(chanew)
    word=''.join(wordlist)
    sentancelist.append(word)
santance=' '.join(sentancelist)
print(santance)
