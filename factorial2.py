# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 05:43:31 2019

@author: Admin
"""

def fact(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product


def fact2(d):
    if(d==0):
        return 1
    else:
        return d*fact2(d-1)
    

n=int(input("n:"))
i=fact2(n)
print("ans:",i)
