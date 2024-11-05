weightInPounds = int(input("Enter weight in pounds: "))
heightInInches = int(input("Enter height in inches: "))

bodyMassIndex = (weightInPounds * 703) / heightInInches * heightInInches;
print("the result is " , bodyMassIndex)


