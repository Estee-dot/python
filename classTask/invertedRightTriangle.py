value = int(input("Enter a number: "))

for count in range(value, 0 , -1):
    for number in range(count, 0 , -1):
        print(number , end = " ")
    print()