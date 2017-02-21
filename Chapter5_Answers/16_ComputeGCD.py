#Program to find the Greatest Common Divisor(GCD) of Two numbers

n1=eval(input("Enter first number: "))
n2=eval(input("Enter second number: "))
GCD = 1

if(n1 < n2):
    smaller = n1
else:
    smaller = n2
  
for i in range(1,smaller + 1):
    if((n1 % i == 0) and (n2 % i == 0)):
        GCD = i

print("The GCD of ", n1 ," and ", n2, " is : ", GCD)