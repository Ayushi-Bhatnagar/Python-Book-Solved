#This program solves 2X2 linear equation using Cramer's rule

a,b,c,d,e,f = eval(input("Enter a,b,c,d,e,f: "))

if(((a*d) - (b*c)) == 0):
    print("This equation has no solution")
else:
    x = ((e*d)-(b*f)) / ((a*d)-(b*c))
    y = ((a*f)-(e*c)) / ((a*d)-(b*c))
    print("x is ",x," and y is ",y)
