base = int(input("enter base: "))

for count in range(1, base + 2):
    for counter in range(1, count):
        print("*", end = " ")
    print()