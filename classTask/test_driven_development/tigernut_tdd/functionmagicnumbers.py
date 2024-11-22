def get_magic_numbers(numbers : list):
    sum = 0
    for count in range(len(numbers)):
        for num in numbers:
            sum += num
        sum -= numbers[count] 
    return sum

