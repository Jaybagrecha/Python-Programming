# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:45:36 2019

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
        
matrix(x,y)