# This program displays a clock showing time 9:15:00
import turtle

turtle = turtle.Turtle()  #To keep the turtle pop up window from closing automatically, remove this line!

#First- Make a circle for the clock 
turtle.penup()
turtle.goto(0,-180)
turtle.pendown()
turtle.circle(180)

#Write the text in the clock 
turtle.penup()
turtle.goto(0,160)
turtle.write("12", font=("Arial", 16, "normal"))
turtle.penup()
turtle.goto(-170,0)
turtle.write("9", font=("Arial", 16, "normal"))
turtle.penup()
turtle.goto(0,-170)
turtle.write("6", font=("Arial", 16, "normal"))
turtle.penup()
turtle.goto(170,0)
turtle.write("3", font=("Arial", 16, "normal"))

#Write the time to be displayed at the bottom 
turtle.penup()
turtle.goto(-8,-200)
turtle.write("9:15:00", font=("Arial", 16, "normal"))

#Hour hand is at 9 
turtle.penup()
turtle.goto(0,0)
turtle.setheading(90) 
turtle.right(270)
turtle.pendown()
turtle.forward(100)

#Minute hand is at 3
turtle.penup()
turtle.goto(0,0)
turtle.setheading(90) 
turtle.right(90)
turtle.pendown()
turtle.forward(150)

#Seconds hand is at 12
turtle.penup()
turtle.goto(0,0)
turtle.setheading(90)
turtle.right(0)
turtle.pendown()
turtle.forward(150)

turtle.done()