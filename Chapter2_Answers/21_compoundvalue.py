#This is a program to find the compounded value on initial savings 
initSavings = eval(input("Enter the monthly saving amount: "))

annualIntRate = 5
monthlyRate = 0.05 / 12

first = initSavings * (1 + monthlyRate)
second = (initSavings + first) * (1 + monthlyRate)
third = (initSavings + second) * (1 + monthlyRate)
fourth = (initSavings + third) * (1 + monthlyRate)
fifth = (initSavings + fourth) * (1 + monthlyRate)
sixth = (initSavings + fifth) * (1 + monthlyRate)

print("After sixth month, the account value is: ", sixth)
