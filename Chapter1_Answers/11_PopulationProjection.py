''' Following is the code for population projector based on following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
'''

Totalsec = 5*365*24*3600 #Calculate no of seconds in 5 years

birth = Totalsec//7 #no of births
death = Totalsec//13 #no of deaths
immigrant = Totalsec//45 #no of immigrants

currentpop = 312032486
popafter5 = currentpop + birth + immigrant - death

print("Current population is:", currentpop)
print("Population after 5 years will be:", popafter5)
