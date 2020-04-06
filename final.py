# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:11:51 2019

@author: Admin
"""

N,U,D=map(int,input().split())

while(N<1 or N>100 and U<1 and D>100000):
    N,U,D=map(int,input().split())
    
    
B=list(map(int,input().split()))

cnt=0
ch=0

for i in range(N-1):
    if(B[i]==B[i+1]):
        cnt=cnt+1
        
    elif(B[i+1]>B[i]):
        if(B[i+1]-B[i]<=U):
            cnt=cnt+1
        else:
            break
    else:
        if(B[i]-B[i-1]<=D):
            cnt=cnt+1
        elif(ch==0):
            cnt=cnt+1
            ch=ch+1
        else:
            break
            
print(cnt+1,end="")

    