#Program to find whether 2 circles overlap or not
import turtle

turtle = turtle.Turtle()

#Enter centers of both circles and their radius:
x1,y1,r1=eval(input("Enter circle1's center x-, y-coordinates, and radius:"))

x2,y2,r2=eval(input("Enter circle2's center x-, y-coordinates, and radius:"))

# Draw circles using the given input
turtle.penup()
turtle.goto(x1,y1-r1)
turtle.pendown()
turtle.circle(r1)
turtle.penup()
turtle.goto(x2,y2-r2)
turtle.pendown()
turtle.circle(r2)
turtle.penup()

d=(((x2-x1)**2)+((y2-y1)**2))**0.5
if d<=abs(r1-r2):
    turtle.write("circle2 is inside circle1",font=("Arial", 12, "normal"))
 
elif d<=r1+r2:
    turtle.write("circle2 overlaps circle1",font=("Arial", 12, "normal"))
else:
    turtle.write("circle2 does not overlaps circle1",font=("Arial", 12, "normal"))
     
turtle.hideturtle()
turtle.done()