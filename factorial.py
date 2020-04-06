# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:11:28 2019

@author: Admin
"""



def factorial(n):
    if(n==0):
        return 1
    fact=n*factorial(n-1)
    return fact
j=int(input("Enter no: "))    
print(factorial(j),end="")