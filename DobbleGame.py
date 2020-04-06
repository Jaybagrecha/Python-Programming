# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:31:01 2019

@author: Admin
"""

import string
import random

symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*5     #CREATING EMPTY LIST OF 5 ELEMENTS
card2=[0]*5
pos1=random.randint(0,4)    #ASSIGN THE POSITION OF SAME SYMBOL IN CARD
pos2=random.randint(0,4)
#print(pos1)
#print(pos2)
x=0
while(1):
    samesymbol=random.choice(symbols)
    symbols.remove(samesymbol)  #REMOVE THE SYMBOL FROM LIST AFTER USING IT
    if(pos1==pos2):
        card1[pos1]=samesymbol
        card2[pos1]=samesymbol
    else:
        card1[pos1]=samesymbol
        card2[pos2]=samesymbol
        card1[pos2]=random.choice(symbols) #WHAT SHOULD BE PLACED AT THE POS2 in CARD1
        symbols.remove(card1[pos2]) 
        card2[pos1]=random.choice(symbols)  #VICE VERSA
        symbols.remove(card2[pos1])
    i=0
    while(i<5):
        if(i!=pos1 and i!=pos2):
            alphabet1=random.choice(symbols)
            symbols.remove(alphabet1)
            alphabet2=random.choice(symbols)
            symbols.remove(alphabet2)
            card1[i]=alphabet1
            card2[i]=alphabet2
        i=i+1
        
    print(card1)
    print(card2)
    ch=input("Enter Right Choice: ")
    if(ch==samesymbol):
        print("RIGHT ANSWER")
        x=x+1
        print("Your Score is ",x)
        c=int(input("Press 0 to quit and 1 to continue: "))
        if(c==0):
            print("Thanks for playing ")
            break
    else:
        print("WRONG ANSWER")
        c=int(input("Press 0 to quit and 1 to continue: "))
        if(c==0):
            print("Thanks for playing ")
            break
    

