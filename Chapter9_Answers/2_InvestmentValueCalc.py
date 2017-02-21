'''Program to create an investment calculator using TkInterface'''
from tkinter import * 

class InvestCalculator:

    def __init__(self):
        window = Tk() 
        window.title("Investment Value Calculator") 
        Label(window, text = "Investment Amount").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "Years").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Annual Interest Rate").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Future Value").grid(row = 4, column = 1, sticky = W)
        
        self.InvestmentAmountVar = StringVar()
        Entry(window, textvariable = self.InvestmentAmountVar, justify = RIGHT).grid(row = 1, column = 2)
        self.YearsVar = StringVar()
        Entry(window, textvariable = self.YearsVar, justify = RIGHT).grid(row = 2, column = 2)
        self.AnnualInterestRateVar = StringVar()
        Entry(window, textvariable = self.AnnualInterestRateVar, justify = RIGHT).grid(row = 3, column = 2)
        self.FutureValueVar = StringVar()
        lblFutureValue = Label(window, textvariable = self.FutureValueVar, justify = RIGHT).grid(row = 4, column = 2)
        btCalculate = Button(window, text = "Calculate", command = self.calculateInvestment, justify = RIGHT).grid(row = 5, column = 2) 
        window.mainloop() # Create an event loop
                
    def calculateInvestment(self):
        monthlyInterestRate = float(self.AnnualInterestRateVar.get())/12
        months = float(self.YearsVar.get()) * 12
        futureValue = float(self.InvestmentAmountVar.get()) * ((1 + monthlyInterestRate)**months)
        self.FutureValueVar.set(format(futureValue, "10.2f"))
    
InvestCalculator()