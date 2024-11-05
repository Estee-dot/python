number = input("enter a five digit number: ")

if number.isdigit():
    for i in number:
        print(i, end = " ")
else:
    print("not a numerical value")