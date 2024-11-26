number = int(input("Enter a number: "))

for count in range(1, number + 1):
    for counter in range(1, count + 1):
        print(counter,  end = " ")
    print()

for countA in range(number, 1, -1):
    for counterA in range(1, countA):
        print(counterA, end = " ")
    print()