choice = 0

while choice != -1:
    first = input("enter first number: ")
    second = input("enter second number: ")
    third = input("enter third number: ")
    fourth = input("enter the fourth number: ")
    if first.isdigit() and second.isdigit() and fourth.isdigit() and third.isdigit():
        first = int(first)
        second = int(second)
        third = int(third)
        fourth = int(fourth)
        sum = (first + second + third + fourth) / 4
        print(f"sum: {first + second + third + fourth}\nAverage: {sum}\nproduct: {first * second * third * fourth}")
        choice = int(input("enter -1 to quit: "))
    else:
        print("value isn't a numerical value")