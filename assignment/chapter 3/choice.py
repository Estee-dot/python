first = int(input("enter first number: "))

largest = first
smallest = first

choice = 1
sum = 0
multiple = 1


while choice <= 3:
    first = input("enter first number: ")
    if first.isdigit():
        first = int(first)
        sum += first
        multiple *= first
        if first > largest:
            largest = first
        elif first < smallest:
            smallest = first
        
    else:
        print("value isn't a numerical value")
    choice += 1
else:
    print(sum)
    print(multiple)
    print(sum/4)
    print(largest)
    print(smallest)