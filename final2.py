# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:25:54 2019

@author: Admin
"""

N=int(input())
while(N<2 and N>100000):
    N=int(input().split())
x=input().split(" ")[:N]

for i in range(len(x)):
    x[i]=int(x[i])
    
temp=0
for i in range(N):
    for j in range(N):
        mod=x[i]%x[j]
        if(mod>temp):
            temp=mod
            
print(temp,end="")