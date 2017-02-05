# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 00:59:12 2017

@author: 张瑞
"""
Uname=['zhangrui','wangshao','zhouyue','shouyi','liuyao','lisicheng','jiyanping']
salary=[5000,20000,12000,14000,10000,60000,10000]
name_salary_zip=zip(Uname,salary)
name_salary_dic=dict(name_salary_zip)

for key in name_salary_dic:
    print 'name:%10s'%key,'salary:%6s'%name_salary_dic[key]
print name_salary_dic.keys()
print name_salary_dic.values()
print name_salary_dic.get('zhangrui')
print name_salary_dic.get('mayun')
name_salary_dic_upd={}
name_salary_dic.update({('mayun',99999),('zhangrui','10000')})
print name_salary_dic
