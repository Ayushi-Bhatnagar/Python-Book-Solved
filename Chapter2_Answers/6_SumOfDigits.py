#Program to calculate the sum of digits of an integer between 0 and 1000

num = eval(input("Enter a number between 0 and 1000: "))

ones = num % 10
rem = num // 10
tens = rem %10
hundreds = rem //10

sumofdigits = hundreds + tens +  ones

print("Sum of digits of ", num, "is ", sumofdigits)