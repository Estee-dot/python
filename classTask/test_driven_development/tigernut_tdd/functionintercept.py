def get_two_list(numberOne, numberTwo):
    intercept = []
    for num in numberOne:
        for newNum in numberTwo:
            if num == newNum:
                intercept.append(num)
    
    return intercept        