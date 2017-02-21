#This program is to estimate the area between 4 different cities using their GPS coordinates

#Atlanta, Georgia Coordinates 
atllat = 33.8201000
atllong = -84.3664700

#Savannah, Georgia Coordinates
savlat =  32.0482400
savlong = -81.1174700

#Charlotte, North Carolina Coordinates
chrlat = 35.2987700
chrlong = -80.8957200

# Orlando, Florida Coordinates
ordlat = 28.5383355
ordlong = -81.3792365

#Distance between Atlanta and Charolette
side1 = ((chrlat - atllat)**2 + (chrlong - atllong)**2)**.5

#Distance between Charolette and Savannah
side2 = ((savlat - chrlat)**2 + (savlong - chrlong)**2)**.5
#Distance between Savannah and Orlando
side3 = ((ordlat - savlat)**2 + (ordlong - savlong)**2)**.5

#Distance between Orlando and Atlanta
side4 = ((atllat - ordlat)**2 + (atllong - ordlong)**2)**.5

#Distance between Charolette and Orlando
diag1 = ((chrlat - ordlat)**2 + (chrlong - ordlong)**2)**.5

#Triangle 1 formed by Atlanta, Charolette and Orlando
s1 = (side1 + side4 + diag1) / 2
area1 = (s1*(s1 - side1)*(s1 - side4)*(s1 - diag1))**.5

print("Area of one triangle is:", area1)

#Triangle 2 formed by Charolette, Savannah and Orlando
s2 = (side2 + side3 + diag1) / 2
area2 = (s2*(s2 - side2)*(s2 - diag1)*(s2 - side3))**.5

print("Area of second triangle is: ", area2)

TotalArea = area1 + area2

print("Estimated area enclosed by Atlanta, Orlando, Savannah and Charolette is: ", TotalArea)


