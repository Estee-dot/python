count = 7

for index in range(1, count + 1):
    print(" " * (count - index), end="")
    for character in range(index):
        print(chr(65 + character), end="")
    for character in range(index - 2, -1, -1):
        print(chr(65 + character), end="")
    print()
    
for index in range(count - 1, 0, -1):
    print(" " * (count - index), end="")
    for character in range(index):
        print(chr(65 + character), end="")
    for character in range(index - 2, -1, -1):
        print(chr(65 + character), end="")
    print()