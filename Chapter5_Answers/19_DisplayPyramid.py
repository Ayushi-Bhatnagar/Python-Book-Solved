#Program to draw a pyramid

N = eval(input("Enter the number of lines: "))

for i in range(1, N+1):  
    for j in range(N-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print("\n")    
