largest = 0
validator = 1

while validator <=10:

    score = int(input("Enter a score {count}: "))
    if score > 0 and score <= 100:
        if score > largest:
            largest = score
            validator +=1
    else:
        print("invalid input! ")
        validator -= 1

print(f"The largest number is {largest}")
