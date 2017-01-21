# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:23:31 2017

@author: 张瑞
"""

f=open(r'E:\test.txt')
cNames=f.readlines()
print cNames
f.close()


f1=open(r'e:\test.txt')
cNames=f1.readlines()
for i in range(0,len(cNames)):
    cNames[i]=str(i+1)+''+cNames[i]
f1.close()
f2=open(r'e:\test3.txt','w')
f2.writelines(cNames)
f2.close()

new_string='zhangrui campany'
f3=open(r'e:\test2.txt','a+')
f3.writelines('\n')
f3.writelines(new_string)
f3.seek(0,0)
read_string=f3.readlines()
print read_string
f3.close()
