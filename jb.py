# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:02:40 2019

@author: Admin
"""

def euclidean(a,b):
    r1=a
    r2=b
    t1=0
    t2=1
    
    while(r2>0):
        q=int(r1/r2)
        r=r1-(q*r2)
        r1=r2
        r2=r
        t=t1-(q*t2)
        t1=t2
        t2=t
    return t1

import sympy
p=int(input("Enter p: "))
while(sympy.isprime(p)==False):
    p=int(input("Enter p such that p is prime: "))
q=int(input("Enter q: "))
while(sympy.isprime(q)==False):
    q=int(input("Enter q such that q is prime: "))
n=p*q
a=p-1
b=q-1
j=a*b
print("J: ",j)
e=int(input("Enter E: "))
#while(math.gcd(j,n)!=1 or e<1 or e>j):
 #e=int(input("Enter E: "))    
d=euclidean(j,e)%n
print("D: ",d)

m=int(input("Enter M: "))
while(m>n):
    m=int(input("Enter M: "))
cip=(m**e)%n
print("ENCRYPTED TEXT ",cip)

k=(cip**d)%n
print("DECRYPTED TEXT ",k)

