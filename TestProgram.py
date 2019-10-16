from gfxhat import lcd
from click import getchar
from reyn0149Library import eraseObject, checkCollision, moveObject

choiceInt = 0
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
        x = random.randint(40,60)
        y = random.randint(20,40)
        vx = random.randint(1,2)
        vy = random.randint(1,2)
        Sx = 128
        Sy = 64
        obj = ball
    elif choiceInt ==2:
        x = input("What should the starting x value be?")
        y = input("What should the starting y value be?")
        vx = input("What should the initial x velocity be?")
        vy = input("What should the initial y velocity be?")
        Sx = input("How wide is your screen in pixels? (Default is 128)")
        Sy = input("How tall is your screen in pixels? (Default is 64)")
        if x > Sx:
            x = 0
        if y > Sy:
            y = 0
        obj = ball
    else:
        print("Sorry! That's not a recognized choice! \n")
        choiceInt = 0
#Start of the bouncing ball program
lcd.clear()
print("Here's your bouncing ball!")
print("Press Control + C to quit")

#Infinite loop (I wanted to try non-blocking inputs but I 
#Didn't want to make my program OS specific)
while userInput != "q":
    eraseObject(obj,x,y)
    collision = checkCollision(obj,x,y,vx,vy,Sx,Sy)
    if collision[0]==1:
        vy = vy*-1
    if collision[1]==1:
        vx = vx*-1
    moveObject(obj,x,y,vx,vy)
    lcd.show()
    x=x+vx
    y=y+vy
