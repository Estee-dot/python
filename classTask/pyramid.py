value = int(input("Enter a number: "))

for counter in range(1, value + 2):
    for count in range(1, counter):
        print(count , end=" ")
    print()

for counterB in range(1, value ):
    for countB in range(10, counterB, -1):
        print(" ", end=" ")
    for countC in range(1, counterB):
        print(countC, end=" ")
    print()
