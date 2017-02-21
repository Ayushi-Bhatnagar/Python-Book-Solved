#Program to create a class Account
class Account:

    def __init__(self):
        self.__balance = 100.0
        self.__id= 0
        self.__annualInterestRate = 0.0
  
    def getMonthlyInterestRate(self):
        return (self.annualInterestRate/100)/12
  
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

    def withdraw(self,amount):
        self.balance=self.balance-amount
 
    def deposit(self,amount):
        self.balance=self.balance+amount
    
def main():
    myaccount=Account()
    myaccount.id=1122
    myaccount.balance=20000
    myaccount.annualInterestRate=4.5
    myaccount.withdraw(2500)
    myaccount.deposit(3000)
    
    print("Account Info: \n Id:",myaccount.id,"\n Balance:",myaccount.balance,"\n Monthly Interest Rate:",myaccount.getMonthlyInterestRate(),\
    "\n Monthly Interest:",myaccount.getMonthlyInterest())

main()