#turtle program to draw a triangle 
import turtle


x,y = eval(input("Enter point for center of rectangle: "))
width, height = eval(input("Enter width and height of the rectangle: "))

turtle= turtle.Turtle()
turtle.color("blue")
turtle.penup()
turtle.goto(x-height/2, y-width/2)
turtle.pendown()
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)

turtle.done()