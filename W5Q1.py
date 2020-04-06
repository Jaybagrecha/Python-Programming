# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:34:53 2019

@author: Admin
"""

n,v1,v2=map(int,input().split())


t1=(1.4141*n)/v1
t2=2*n/v2

if(v1>=1 and v2<=100 and 1<=n<=200):
    if(t1<t2):
        print("Walking")
    else:
        print("Car")
else:
    print("Invalid")
