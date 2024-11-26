def sum_of_multiples(number):
	sum = 0

    for num in range(first_num, second_num + 1 ):
        sum += num
    return sum
print(sum_of_multiples(number))


first_num = int(input("Enter a number: "))
second_num = int(input("Enter a number: "))
