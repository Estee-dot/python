number = 7

for count in range(1, number + 1):
    print(" " * (number - count), end="")
    for index in range(1, count + 1):
        print(index, end="")
    for index in range(count - 1, 0, -1):
        print(index, end="")
    print()
    
for count in range(number - 1, 0, -1):
    print(" " * (number - count), end="")
    for index in range(1, count + 1):
        print(index, end="")
    for index in range(count - 1, 0, -1):
        print(index, end="")
    print()