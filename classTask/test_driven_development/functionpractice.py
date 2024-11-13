def get_product(first_number, second_number):
    result = 0
    if type(first_number) is int and type(second_number) is int:
        if first_number < 0 and second_number < 0:
            first_number, second_number = abs(first_number), abs(second_number)
        if first_number < 0:
            first_number, second_number = second_number, first_number
        for number in range(first_number):
            result += second_number
        return result

    raise TypeError