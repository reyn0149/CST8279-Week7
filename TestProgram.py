choiceInt = 0
from gfxhat import lcd
from click import getchar
from reyn0149Library import eraseObject, checkCollision, moveObject
userInput = ""
collision =[0,0]
ball =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]

#Start of the user menu
print("Hi! Welcome to my test program")
print("This program tests a simple bouncing ball animation")
print("You can either test with a random set of variables or input your own\n")

while choiceInt == 0:
    print("Would you like random variables or custom ones?")
    print("1 = Random")
    print("2 = Custom\n")
    choiceString = input("")
    try:
        choiceInt =int(choiceString)
    except:
        print("Invalid input! Please try again.")

    if choiceInt ==1:
        import random
        x = random.randint(1,127)
        y = random.randint(1,63)
        vx = random.randint(1,5)
        vy = random.randint(1,5)
        obj = ball
    elif choiceInt ==2:
        x = input("What should the starting x value be?")
        y = input("What should the starting y value be?")
        vx = input("What should the initial x velocity be?")
        vy = input("What should the initial y velocity be?")
        Sx = input("How wide is your screen in pixels? (Default is 128)")
        Sy = input("How tall is your screen in pixels? (Default is 64)")
        obj = ball
    else:
        print("Sorry! That's not a recognized choice! \n")
        choiceInt = 0
#Start of the bouncing ball program
lcd.clear
print("Here's your bouncing ball!")
print("If you'd like to quit, please press q on your keyboard")

while userInput != "q":
    userInput = getchar()
    eraseObject(obj,x,y)
    collision = checkCollision(obj,x,y,vx,vy,Sx,Sy)
    if collision[0]==1:
        vy = vy*-1
    if collision[1]==1:
        vx = vx*-1
    moveObject(obj,x=0,y=0,vx=0,vy=0)
    