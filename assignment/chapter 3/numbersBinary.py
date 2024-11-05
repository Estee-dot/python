number = int(input("enter a number: "))
remainder = 0
binary = " "

while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number // 2

print(binary)