#Program to draw the square function
import turtle

turtle = turtle.Turtle()  #To keep the turtle pop up window from closing automatically, remove this line!


# Draw X and Y axis 
turtle.penup()
turtle.goto(-130, 0)
turtle.pendown()
turtle.goto(130, 0)

turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.goto(0, 80)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.write("Y") 
turtle.penup()
turtle.goto(130, -15)
turtle.pendown()
turtle.write("X") 

turtle.degrees()
turtle.penup()
turtle.goto(130, 0)
turtle.pendown()
turtle.setheading(150)
turtle.forward(20)
turtle.penup()
turtle.goto(130, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.setheading(240)
turtle.forward(20)
turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.setheading(-60)
turtle.forward(20)

# Draw a square function
x = -80
turtle.penup()
turtle.goto(x,  x*x*0.01)
turtle.pendown()
for  x in range(-80, 80 + 1):
    turtle.goto(x, x*x*0.01)


turtle.done()
