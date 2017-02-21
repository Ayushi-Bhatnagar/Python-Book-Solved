#This is a code to draw a star with inner angle 36 degrees
import turtle

turtle = turtle.Turtle()  #To keep the turtle pop up window from closing automatically, remove this line!


turtle.forward(200) #Side length of the star
turtle.right(144)  #Since inner angle 36 degree, outer angle = 180-36 = 144
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
       
turtle.done()

