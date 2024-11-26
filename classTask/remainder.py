number = int(input("Enter a number: "))
sum = 0

while number > 5:
    remainder = first_number % 10
    sum = sum + remainder
    first_number = first_number // 10
print(sum)

