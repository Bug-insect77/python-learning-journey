"""
snake = 0
water =1;
gun=-1;

"""

import random


game_dict = {
    's':0,
    'w':1,
    'g':-1
}
computer = random.choice([1,0,-1])
yourchoice = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
yourmove = game_dict[yourchoice]

if(yourmove==0 and computer==1):
    print("You win")
elif(yourmove==0 and computer==-1):
    print("You loose")    
elif(yourmove==1 and computer==0):
    print("You loose")
elif(yourmove==1 and computer==-1):
    print("You win")    
elif(yourmove==-1 and computer==1):
    print("You loose")
elif(yourmove==-1 and computer==0):
    print("You win")
elif(yourmove==computer):
    print("DRAW")  
else:
    print("something went wrong")              
