number = int(input("enter a number: "))
largest = number
second_largest = 0
counter = 1

while counter <= 10:
    number = int(input("enter a number: "))
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number
    counter += 1

print(largest)
print(second_largest)