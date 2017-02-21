#Program to find the future tuition and its future value

Tuition=10000
Sum = 0
i = 1
j = 1

#calculate Tuition after 10 years

while i<=10:
    Tuition=(Tuition*105)/100
    i+=1

TotalTuition = Tuition

#Tuition for 4 years after 10th year

while j<= 4:
    Tuition=(Tuition*105)/100
    j+=1
    Sum+=Tuition

print("The tuition in 10 years is",format(TotalTuition,".2f"))  

print("Total cost of four years’ worth of tuition starting ten years from now is",format(Sum,".2f"))
  
