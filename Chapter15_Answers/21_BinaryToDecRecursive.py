'''Program to convert from Binary to decimal using recursive method'''
import math

def BinToDec(binstr):
    n=0
    if(binstr[0] == "1" ):
        n=1
    else:
        n=0
        
    if(len(binstr) == 1):
        return n
    
    return math.pow(2, len(binstr)-1)*n + BinToDec(binstr[1:])



def main():
    bin1 = input("Enter binary number: ")
    print("Decimal equivalent is: ", BinToDec(bin1))
    

main()  