#Program to calculate the sum of the given series

Sum = 0
i=1

while i<=49:
    Sum += (( 2*i - 1 ) / ( 2*i + 1 ))
    i=i+1
    
print("Sum of the given series is : ",Sum) 
