#Program to calculate the number of years and days from the given minutes

mins = eval(input("Enter the number of minutes: "))


years = mins// (365*60*24)
rem = mins % (365*60*24)
days = rem// (60*24)


print( mins, "minutes is approximately ", years, "years and ", days," days")