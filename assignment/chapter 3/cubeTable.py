 print("Number \tSquare \tCube")
square = 0
for count in range(0, 6):
    square = count ** 2
    print(f"{count:>5} \t{square:>5} \t{count ** 3:>5}", end=" ")
    print()


