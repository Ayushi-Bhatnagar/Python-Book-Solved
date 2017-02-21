#Program to draw two circles and check whether they overlap or not

#Enter centers of both circles and their radius:
x1,y1,r1=eval(input("Enter circle1's center x-, y-coordinates, and radius:"))

x2,y2,r2=eval(input("Enter circle2's center x-, y-coordinates, and radius:"))

#Distance between centers
d=(((x2-x1)**2)+((y2-y1)**2))**0.5


if d <= abs(r1-r2):
    print("circle2 is inside circle1")
elif d<= r1+r2:
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")