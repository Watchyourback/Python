# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:03:38 2017

@author: 张瑞
"""
#enumerate
seq1=[1,2,3,5,7,2,4,5,0,9,3]
for j1,i1 in enumerate(seq1):
    print j1,i1
seq2='abcdefg'
for i2 in enumerate(seq2):
    print i2
#sort reverse
seq1.sort()
print seq1
seq1.reverse()
print seq1
#zip
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print xyz