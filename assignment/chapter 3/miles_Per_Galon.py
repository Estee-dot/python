ultimate_miles = 0
choice = 0
while choice != -1:
    miles_driven = float(input("enter miles driven: "))
    gallons = float(input("enter gallons: "))
    miles_per_galon = miles_driven / gallons
    ultimate_miles += miles_per_galon
    print(miles_per_galon)
    choice = int(input("enter -1 to quit or 0 to continue: "))

else:
    print(ultimate_miles)