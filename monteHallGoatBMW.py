# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 00:20:07 2019

@author: Admin
"""

import random
doors=[0]*3
goatdoors=[0]*2
swap=0
dont_swap=0
j=0
while(j<10):
    x=random.randint(0,2)
    doors[x]='BMW'

    
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]='goat'
            goatdoors.append(i)
    choice=int(input("Enter Input Choice NO.: "))
    door_open=random.choice(goatdoors)
    while(door_open==choice):
        door_open=random.choice(goatdoors)
    z=input("Do you want to swap (y/n)")
    if(z=='y'):
        if(doors[i]=='goat'):
            print("YOU HAVE WON")
            swap=swap+1
        else:
            print("YOU HAVE LOST")
    else:
         if(doors[i]=='goat'):
            print("YOU HAVE LOST")
         else:
            print("YOU HAVE WIN")
            dont_swap=dont_swap+1
    j=j+1

print(swap)
print(dont_swap)