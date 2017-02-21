import turtle
from random import randint

turtle = turtle.Turtle()  #To keep the turtle pop up window from closing automatically, remove this line!

def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def writeText(s, x, y): 
    turtle.penup() 
    turtle.goto(x, y)
    turtle.pendown() 
    turtle.write(s) 

def drawPoint(x, y): 
    turtle.penup() 
    turtle.goto(x, y)
    turtle.pendown() 
    turtle.begin_fill() 
    turtle.circle(4) 
    turtle.end_fill()

def drawCircle(x, y, radius): 
    turtle.penup() 
    turtle.goto(x, y - radius)
    turtle.pendown() 
    turtle.circle(radius) 
    
def drawRectangle(x, y, width, height): 
    turtle.penup() 
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() 
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)

def main():
    drawRectangle(-75, 0,100, 100)
    drawCircle(50, 0, 50)

    for i in range (10):    
        random1=randint(-100, -30)
        random2=randint(-20, 20)
        turtle.penup()
        turtle.goto(random1,random2)
        turtle.pendown()
        turtle.dot(4)
        turtle.penup()
         
    for i in range (10):    
        random3=randint(30, 75)
        random4=randint(-25, 25)
        turtle.penup()
        turtle.goto(random3,random4)
        turtle.pendown()
        turtle.dot(4)
    
    turtle.done

main()
