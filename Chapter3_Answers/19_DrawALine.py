import turtle

turtle = turtle.Turtle()

x1,y1,x2,y2 = eval(input("Enter x and y values of two different points: "))

turtle.penup()
turtle.goto(x1,y1) #go to (x1,y1)
turtle.pendown()
turtle.write(turtle.pos()) #write coordinates
turtle.goto(x2,y2) # go to (x2,y2)
turtle.write(turtle.pos()) #write coordinates

turtle.done()
