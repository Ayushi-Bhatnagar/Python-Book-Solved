#Program to print the matrix of 0's and 1s
import random

def printMatrix(num):
    while num!=0:
        print(random.randint(0,1),random.randint(0,1),random.randint(0,1))
        num-=1
    return 

def main():
    n=eval(input("Enter n:"))
    printMatrix(n)

main()
