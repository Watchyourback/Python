# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:16:43 2017

@author: 张瑞
"""

from math import sqrt
def isprime(x):
     if x == 1: 
         return False
     k = int(sqrt(x))
     for j in range(2,k+1): 
           if x%j == 0:
                 return False 
     return True
if __name__ == "__main__":
    flag = 'y'
    while(flag == 'y'):
        num = input("Please input a number:")
        for i in range(2,num):
            if isprime(i) and num % i ==0:
                print i,
        flag = raw_input("\nIf you want to input another number,input y please or input n.")