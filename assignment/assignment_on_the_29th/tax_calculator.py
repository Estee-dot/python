total = 0
counter = 1
taxAmount = 0
nameCounter = 1
  
while nameCounter <= 3:
    citizenName = int(input("Enter name: "))       
        nameCounter = nameCounter + 1
   
while counter <= 3:
    citizenEarning = int(input("Earnings: "))                   
        counter = counter + 1;
       
if citizenEarning <= 30000:
    taxAmount = citizenEarning * 0.15
	  total = total + taxAmount        
else if citizenEarning > 30000:
    taxAmount = citizenEarning * 0.20
        total = total + taxAmount
       
print("The total taxes for the three citizens is: ", total)

   
