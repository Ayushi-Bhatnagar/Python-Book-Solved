#Program to draw the sine and cosine functions
import turtle
import math

turtle = turtle.Turtle()  #To keep the turtle pop up window from closing automatically, remove this line!

# Draw X and Y axis
turtle.penup()
turtle.goto(-220, 0)
turtle.pendown()
turtle.goto(220, 0)

turtle.degrees()
turtle.setheading(150)
turtle.forward(20)

turtle.penup()
turtle.goto(220, 0)
turtle.pendown()
turtle.setheading(-150)
turtle.forward(20)

turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.goto(0, 80)

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

turtle.penup()
turtle.goto(-100, -15)
turtle.pendown()
turtle.write("-2π")

turtle.penup()
turtle.goto(100, -15)
turtle.pendown()
turtle.write("2π")

# Sine function in Red
x = -175
turtle.penup()
turtle.goto(x, 50 * math.sin((x / 100.0) * 2 * math.pi))
turtle.pendown()
turtle.color("red")

for x in range(-175, 176): 
    turtle.goto(x, 50 * math.sin((x / 100.0) * 2 * math.pi))


#Draw Cos Function
x = -185
turtle.penup()
turtle.goto(x, 50*math.cos((x / 100.0) * 2 * math.pi))
turtle.pendown()
turtle.color("blue")

for x in range(-185, 186): 
    turtle.goto(x, 50*math.cos((x / 100.0) * 2 * math.pi))


turtle.done()
