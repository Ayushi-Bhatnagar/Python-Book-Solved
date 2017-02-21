#Program to draw a chess board
import turtle

turtle = turtle.Turtle()  #To keep the turtle pop up window from closing automatically, remove this line!

turtle.penup() 
turtle.goto(-120, -120)
turtle.pendown() 
turtle.color("black")

for i in range(4):
    turtle.forward(240) 
    turtle.left(90) 

for j in range(-120, 90, 60): 
    for k in range(-120, 120, 60):
        turtle.penup()
        turtle.goto(k, j)
        turtle.pendown()

      
        turtle.begin_fill()
        for l in range(4):
            turtle.forward(30) 
            turtle.left(90) 
        turtle.end_fill()

for m in range(-90, 120, 60): 
    for n in range(-90, 120, 60):
        turtle.penup()
        turtle.goto(n, m)
        turtle.pendown()
      
        turtle.begin_fill()
        for o in range(4):
            turtle.forward(30) 
            turtle.left(90) 
        turtle.end_fill()


turtle.done() 