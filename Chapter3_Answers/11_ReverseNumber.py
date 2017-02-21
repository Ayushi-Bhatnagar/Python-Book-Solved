#This program takes a 4 digit integer as an input and gives its reverse number as output

N = eval(input("Enter an integer: "))
newNum= ""

#Extract each character and add to a string in reverse order(4 times)
temp = N%10
newNum += str(temp)
N = N//10
temp = N%10
newNum += str(temp)
N = N//10
temp = N%10
newNum += str(temp)
N = N//10
temp = N%10
newNum += str(temp)
N = N//10


print("The reversed number is: ", newNum)
