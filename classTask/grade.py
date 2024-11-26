
passed = 0
failed = 0

for grade in range(1, 16):
    score = int(input("Enter your score: "))

    if score >= 45:
        passed = passed + 1
    else:
        failed = failed + 1
    print(f"number of passes are {passed}")
    print(f"number of fails are {failed}")
