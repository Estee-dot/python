def get_average(number : list):
    average = 0
    sum = 0
    for num in number:
        sum += num
    average = sum // len(number)
    return average
