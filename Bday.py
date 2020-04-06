# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:51:55 2019

@author: Admin
"""
import random
import datetime
birthday=[]
i=0
while(i<50):
    month=random.randint(1,12)    
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        day=random.randint(1,31)
        year=random.randint(1950,2050)
        #print(day,"/",month,"/",year)
    elif(month==4 or month==6 or month==9 or month==11):
        day=random.randint(1,30)
        year=random.randint(1950,2050)
        #print(day,"/",month,"/",year)
    else:
        year=random.randint(1950,2050)
        #year=int(input("Enter year"))
        if(year%4==0 and year%100!=0 or year%400==0):
           # print("Its a leap Year")
            day=random.randint(1,29)
            #print(day,"/",month,"/",year)
        else:
            day=random.randint(1,28)
            #print(day,"/",month,"/",year)
    
    dd=datetime.date(year,month,day)
    #print(dd)
    day_of_year=dd.timetuple().tm_yday
    #print(day_of_year)
    i=i+1
    birthday.append(day_of_year)
#print(birthday)
birthday.sort()
print(birthday)    
    
        
        


