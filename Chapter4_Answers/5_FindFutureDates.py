#This program is to predict future days depending on the day today

Today = eval(input("Enter today's day: ")) 
N = eval(input("Enter the number of days elapsed since today: "))
FutureDay = (N % 7) + Today
StrToday = ""

#Assign day to input
if Today == 0:
    StrToday = "Sunday"
elif Today == 1:
    StrToday = "Monday"
elif Today == 2:
    StrToday = "Tuesday"
elif Today == 3:
    StrToday = "Wednesday"
elif Today == 4:
    StrToday = "Thursday"
elif Today == 5:
    StrToday = "Friday"
elif Today == 6:
    StrToday= "Saturday"
else:
    print("Incorrect input")

# Print result - future day
if FutureDay == 0:
    print("Today is " + StrToday + " and the future day is Sunday" )
elif FutureDay == 1:
    print("Today is " + StrToday + " and the future day is Monday" )
elif FutureDay == 2:
    print("Today is " + StrToday + " and the future day is Tuesday" )
elif FutureDay == 3:
    print("Today is " + StrToday + " and the future day is Wednesday" )
elif FutureDay == 4:
    print("Today is " + StrToday + " and the future day is Thursday" )
elif FutureDay == 5:
    print("Today is " + StrToday + " and the future day is Friday" )
elif FutureDay == 6:
    print("Today is " + StrToday + " and the future day is Saturday" )
else:
    print("Incorrect input")
