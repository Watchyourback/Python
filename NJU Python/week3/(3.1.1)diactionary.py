# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 22:10:14 2017

@author: 张瑞
"""

names=['zhangrui','wangsaho','shouyi']
salary=[10,9,8]
print salary[names.index('zhangrui')]

#字典形式

print 'zip',zip(names,salary)
print 'dic',dict(zip(names,salary))


Adic={'zhangrui':10,'wangshao':9,'shouyi':8}
print Adic['zhangrui'],'\n',Adic


Bdic=dict(zhangrui=10,wangshao=9,shouyi=8)
print Bdic['wangshao']


Cdic={}.fromkeys(('zhangrui','wangshao','shouyi'),3000)
print Cdic
print sorted(Cdic)