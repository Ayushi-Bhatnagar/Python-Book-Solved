#Program to play lottery game
import random

LotteryNum = random.randint(100,999) #Generate random lottery number

InputNum = eval(input("Enter your lottery pick (3 digits): "))

#Extract digits of lottery number
lotteryLast = LotteryNum % 10
Rem = LotteryNum % 100
lotterySecond = Rem // 10
lotteryFirst = LotteryNum // 100

#Extract digits of input number
InputLast = InputNum % 10
Rem1 = InputNum % 100
InputSecond = Rem1 // 10
InputFirst = InputNum // 100

print("The Lottery number is: ",LotteryNum)

if LotteryNum == InputNum:
    print("Exact Match: you win $10,000")
elif ((lotteryLast == InputLast) or (lotteryLast == InputSecond) \
    or (lotteryLast == InputFirst)) and ((lotterySecond == InputLast) \
    or (lotterySecond == InputSecond) or (lotteryFirst == InputFirst)) \
    and ((lotteryFirst == InputLast) or (lotteryFirst == InputSecond) \
    or (lotteryFirst == InputFirst)):
        print("Match all digits: you win $3,000")
elif ((lotteryLast == InputLast) or (lotteryLast == InputSecond) \
    or (lotteryLast == InputFirst) or (lotterySecond == InputLast) \
    or (lotterySecond == InputSecond) or (lotteryFirst == InputFirst) \
    or (lotteryFirst == InputLast) or (lotteryFirst == InputSecond) \
    or (lotteryFirst == InputFirst)):
        print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
