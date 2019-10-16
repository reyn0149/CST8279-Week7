#A function that erases all pixels that match an object
def eraseObject(obj,x=0,y=0):
    from gfxhat import lcd
    initialX = x

    for i in range(len(obj)):
        row =obj[i]
        y = y+1
        x = initialX
        for i in range (len(row)):
            if row[i] == 1:
                lcd.set_pixel(x,y,0)
            x = x+1

#A function that moves an object across the screen
def moveObject(obj,x=0,y=0,vx=0,vy=0):
    from gfxhat import lcd
    #Moving the object based on vx and vy
    x = x+vx
    y = y+vy
    initialX = x

    for i in range(len(obj)):
        row =obj[i]
        y = y+1
        x = initialX
        for i in range (len(row)):
            if row[i] == 1:
                lcd.set_pixel(x,y,1)
            x = x+1    

#A function that checks if an object has reached the edge of the gfxhat
def checkCollision(obj,x=0,y=0,vx=0,vy=0,Sx=128,Sy=64):
    collisionTuple =[0,0]
    #checks to see if the object is going off the top or bottom of the screen
    if y+vy < 0 or y+vy+len(obj)+1> Sy:
        collisionTuple[0] = 1
    #checks to see if the object is going off the left or right of the screen
    if x+vx < 0 or x+vx+len(max(obj)) > Sx:
        collisionTuple[1] = 1
    return(collisionTuple)
   
