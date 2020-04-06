# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:37:50 2019

@author: Admin
"""

import random

movies=['Lagaan','anand','3 ididots','Dangal','Sultan','Rang de basanti','Gangs of wasseypur','Swades','Taare Zameen Par','Zindagi Na Milegi Dobaara','Special 26','Dil Chahta Hai','Queen','Drishyam','Barfi','Guru']

def create_qn(movie):
    n=len(movie)    # to open movie('movies list') in a list of characters
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn
    
def is_present(letter,movie):
    c=movie.count(letter)
    if(c==0):
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if(ref[i]==' ' or ref[i]==letter):
            temp.append(ref[i])
        else:
            if(qn_list[i]=='*'):
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new

def play():
    
    p1=input("Enter name of player 1: ")
    p2=input("Enter name of player 2: ")
    pp1=0
    pp2=0
    turn=0
    willing=True
    
    while(willing):
        
        if(turn%2==0):
            print("Your Turn ",p2)
            picked_movie=random.choice(movies)
            qn=create_qn(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while(not_said):
                letter=input("Guess the letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to Guess the movie and 2 to enter another character"))
                    if(d==1):
                        ans=input("Enter your answer")
                        if(ans==picked_movie):
                            print("Right answer")
                            pp2=pp2+1
                            not_said=False
                            print("Total score is ",pp2)
                        else:
                            print("Wrong answer,Try again")
                                
                else:
                    print(letter,"not found")
            c=int(input("Press 1 to continue and 0 to quit"))
            if(c==0):
                print("Thanks for playing ",p1," Your Final Score is ",pp1)
                print("Thanks for playing ",p2," Your Final Score is ",pp2)
                willing=False
        else:
            print("Your Turn ",p1)
            picked_movie=random.choice(movies)
            qn=create_qn(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while(not_said):
                letter=input("Guess the letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to Guess the movie and 2 to enter another character"))
                    if(d==1):
                        ans=input("Enter your answer")
                        if(ans==picked_movie):
                            print("Right answer")
                            pp1=pp1+1
                            not_said=False
                            print("Total score is ",pp1)
                        else:
                            print("Wrong answer,Try again")
                                
                else:
                    print(letter,"not found")
            c=int(input("Press 1 to continue and 0 to quit"))
            if(c==0):
                print("Thanks for playing ",p1," Your Final Score is ",pp1)
                print("Thanks for playing ",p2," Your Final Score is ",pp2)
                willing=False
        turn=turn+1
play()

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            