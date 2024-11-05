binary = int(input("enter a binary number: "))
power = 1
number = 0


while binary > 0:
    number_one = binary % 10
    number += number_one * power
    power *= 2
    binary = binary // 10

print(number)
