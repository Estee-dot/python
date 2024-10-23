number1 = int(input("Enter a three digit integer: "))
digit1 = number1 / 100
number2 = number1 / 10
digit2 = number2 % 10
digit3 = number1 % 10

if digit1 == digit3:
    print(f" %d is a Palindrome" {number1})
else:
    print(f"%d is not a Palindrome" {number1})
