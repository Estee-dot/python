number = int(input("enter a number: "))
factorial = 1

for count in range(1, number + 1):
    factorial *= (number + 1) - count
    print((number + 1) - count, end = " ")


print()
print(f"factorial: {factorial}")