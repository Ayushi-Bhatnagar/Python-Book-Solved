#Enter scores of students in class and find highest and second highest score
Total = eval(input("Enter the number of students: "))

high = 0
sec = 0

for i in range(Total):
    score = eval(input("Enter student score "+ str(i+1) +": ")) 

    if score > high:
        sec = high
        high= score
    elif score > sec:
        sec = score

print("Highest Marks: ",high)
print("Second Highest Marks: ", sec)