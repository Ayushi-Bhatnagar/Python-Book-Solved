#This program is to draw different shapes using Turtle graphics
import turtle

turtle = turtle.Turtle()

turtle.penup()
turtle.goto(-300,0)

#Draw a Triangle
turtle.pendown()
turtle.begin_fill() 
turtle.color("black")
turtle.left(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()

#Draw a Square
turtle.penup()
turtle.goto(-180,0)
turtle.pendown()
turtle.begin_fill() 
turtle.color("black")
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.end_fill()

#Draw a Pentagon
turtle.penup()
turtle.goto(-60,0)
turtle.pendown()
turtle.begin_fill() 
turtle.color("black")
turtle.right(72)
turtle.forward(60)
turtle.right(72)
turtle.forward(60)
turtle.right(72)
turtle.forward(60)
turtle.right(72)
turtle.forward(60)
turtle.right(72)
turtle.forward(60)
turtle.end_fill()

#Draw a Hexagon
turtle.penup()
turtle.goto(50,0)
turtle.pendown()
turtle.begin_fill() 
turtle.color("black")
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.end_fill()

#Draw a Octagon
turtle.penup()
turtle.goto(160,0)
turtle.pendown()
turtle.begin_fill() 
turtle.color("black")
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(40)
turtle.right(45)
turtle.forward(40)
turtle.end_fill()



turtle.done()
