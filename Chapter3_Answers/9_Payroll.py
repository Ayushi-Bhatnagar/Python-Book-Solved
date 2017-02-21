#This program takes an employee information and returns a payroll statement 

#Input information from Employee
EmpName = input("Enter employee's name: ")
HoursPerWeek = eval(input("Enter number of hours worked in a week: "))
PayRate = eval(input("Enter hourly pay rate: "))
FedTax = eval(input("Enter federal tax withholding rate: "))
StateTax = eval(input("Enter state tax withholding rate: "))

#Calculate Payroll statement variables
NewFedTax = FedTax*100 #Federal Tax
NewStateTax = StateTax*100 #State Tax
TotalEarning = PayRate * HoursPerWeek #Total Earning
FedTaxDed = (NewFedTax/100) * TotalEarning #Federal Tax Deduction
StateTaxDed = (NewStateTax/100) * TotalEarning #State Tax Deduction
TotalDed= FedTaxDed + StateTaxDed #TotalDeduction
NetPay = TotalEarning -  TotalDed #NetPay

#Print payroll statement
print("Employee name: ",EmpName)
print("Hours worked: ",HoursPerWeek)
print("Pay Rate: $"+str(PayRate))
print("Gross Pay: $"+str(TotalEarning))
print("Deductions:")
print("Federal Withholding (" + str(NewFedTax) +"%): $" +str(FedTaxDed))
print("State Withholding (" + str(NewStateTax) +"%): $" +str(StateTaxDed))
print("Total Deductions: $" + str(TotalDed))
print("Net Pay: $" + str(NetPay))
