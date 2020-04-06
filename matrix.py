# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:34:57 2019

@author: Admin
"""

def matrix(n,m):
    mat=[]
    count=1
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(count)
            count +=1
        mat.append(l)
        
    for i in range(n):
        for j in range(m): 
            print(mat[i][j],end=" ")
        print()
        
x,y=map(int,input().split())
matrix(x,y)
