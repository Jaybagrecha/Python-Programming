import random

def choose():
   #x=list(map(int,input("Enter the list to choose from: ").split()))
   x=list(input("Enter the list to choose from: ").split())
   #x=['jay','janvi','pranali','karthik','purvi','hardik','harsh']
   pick=random.choice(x)
   return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))  #mod3permutationsJumbledWord3 
    #join(random.sample) function is used for rearranging the picked word
    #random.sample will rearrange the letters 
    #and join will join the letters as a word
    return jumbled
    

def play():
    p1name=input('Enter your name player 1: ')
    p2name=input('Enter your name player 2: ')
    pp1=0
    pp2=0
    turn=0
    
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        
        if(turn%2==0):
            print(p1name,"Player 1 play ")
            ans=input("Enter Answer: ")
            if(ans==picked_word):
                pp1=pp1+1
                print("Right Answer, Total Points are: ",pp1)
            else:
                print("Wrong Answer mate! This is the right answer ",picked_word)
            c=int(input("Press 0 to quit and 1 to continue: "))
            if(c==0):
                print("Thanks for playing ",p1name,p2name,"\n Your Final Score is :","player 1: ",pp1,"player 2: ",pp2)
                break
            
        else:
            print(p2name,"Player 2 play ")
            ans=input("Enter Answer")
            if(ans==picked_word):
                pp2=pp2+1
                print("Right Answer, Total Points are: ",pp2)
            else:
                print("Wrong Answer mate! This is the right answer ",picked_word)
            c=int(input("Press 0 to quit and 1 to continue: "))
            if(c==0):
                print("Thanks for playing ",p1name,p2name,"\n Your Final Score is :","player 1: ",pp1,"player 2: ",pp2)
                break
        turn=turn+1    
play()