#This is a program to find the area of a triangle
x1,y1,x2,y2,x3,y3 = eval(input("Enter three points for a triangle: "))

side1 = ((x1-x2)**2 + (y1-y2)**2)**.5
side2 = ((x2-x3)**2 + (y2-y3)**2)**.5
side3 = ((x3-x1)**2 + (y3-y1)**2)**.5

s = (side1 + side2 + side3)/2
area = (s*(s-side1)*(s-side2)*(s-side3))**.5

print("area of triangle is : ", area)