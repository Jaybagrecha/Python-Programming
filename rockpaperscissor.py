# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:01:50 2019

@author: Admin
"""
def rock_paper_scissor(num1,num2,bit1,bit2):
    #pp1=0
    #pp2=0
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3

    if(player1[p1]=='Rock' and player2[p2]=='Scissor' or player1[p1]=='Paper' and player2[p2]=='Rock' or player1[p1]=='Scissor' and player2[p2]=='Paper'):
        print("Player 1 wins")
        #pp1=pp1+1
        #print("Score-> ",pp1)
        
        
    if(player2[p2]=='Rock' and player1[p1]=='Scissor' or player2[p2]=='Paper' and player1[p1]=='Rock' or player2[p2]=='Scissor' and player1[p1]=='Paper'):
        print("Player 2 wins")
       # pp2=pp2+1
        #print("Score-> ",pp2)
        
    else:
        print("Draw")
   


player1={0:'Rock',1:'Paper',2:'Scissor'}
player2={0:'Rock',1:'Paper',2:'Scissor'}
while(True):
    num1=input("Player 1,Enter your secret string: ") 
    num2=input("Player 2,Enter your secret string: ")
    bit1=int(input("player1, Enter your bit position: "))
    while(bit1>=len(num1)):
        bit1=int(input("player1, Please Enter valid bit position: "))
    bit2=int(input("player2, Enter your bit position: "))
    while(bit2>=len(num1)):
        bit2=int(input("player1, Please Enter Valid bit position: ")) 
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=int(input("Do you want to countinue(1/0)"))
    if(ch==0):
        break
    

    