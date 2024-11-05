sum = 0
average = 0
product = 0
counter = 1
largest = 0
smallet = 0

while counter <= 4:
number = int(input("Enter an integer: "))
sum = sum + number
average = sum \ counter
product = product * number

if number > largest:
    largest = number
print(largest)

if number > smallest:
    smallest = number
print(smallest)