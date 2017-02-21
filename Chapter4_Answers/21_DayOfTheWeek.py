#Finding day of the week using Zeller's Congruence
'''
According to the Zeller's congruence formula:

h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday, 4: Wednesday, 5: Thursday, 6: Friday).
q is the day of the month.
m is the month (3:March,4:April,...,12:December).
j is the century.
k is the year of the century (i.e.,year%100).

'''
import math

Year = eval(input("Enter year: (e.g., 2008): "))
m = eval(input("Enter month: 1-12 : ")) 
q = eval(input("Enter the day of the month: 1-31 : "))

j = math.floor(Year / 100)
k = Year % 100 

h = (q + math.floor((26*(m + 1))/10) + k + math.floor(k/4) + math.floor(j/4) + (5 * j)) % 7

if h == 0:
    print("Day of the Week is Saturday")
elif h == 1:
    print("Day of the Week is Sunday")
elif h == 2:
    print("Day of the Week is Monday")
elif h == 3:
    print("Day of the Week is Tuesday")
elif h == 4:
    print("Day of the Week is Wednesday")
elif h == 5:
    print("Day of the Week is Thursday")
elif h == 6:
    print("Day of the Week is Friday")
else:
    print("Incorrect Input")
