#This program is calculate the gratuity and total
subtotal, gratuityrate = eval(input("Enter the subtotal and gratuity rate: "))

gratuity = subtotal * gratuityrate/100 
total = subtotal + gratuity

print("The gratuity is ",gratuity,"and the total is ", total)
