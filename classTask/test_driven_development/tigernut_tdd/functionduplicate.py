def get_duplicate(numbers):
    for num in numbers:
        for numOne in numbers:
            counter = 0
            if num == numOne:
                counter += 1
                    if counter >= 2:
                        return True
                            break
   if counter < 2: return False
   