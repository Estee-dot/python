print("pattern a")
for counter in range(1, 11):
    for count in range(1, counter):
        print("*", end=" ")
    print()

print()
print("pattern b")
for counterA in range(1, 11):
    for countA in range(10, counterA, -1):
        print("*", end=" ")
    print()

print()
print("pattern c")
for counterB in range(1, 11):
    for countB in range(10, counterB, -1):
        print(" ", end=" ")
    for countC in range(1, counterB):
        print("*", end=" ")
    print()

print()
print("pattern d")
for counterD in range(1, 11):
    for countD in range(1, counterD):
        print(" ", end=" ")
    for countE in range(10, counterD, -1):
        print("*", end=" ")
    print()



 