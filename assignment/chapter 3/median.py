import statistics


sum =  9 + 11 + 22 + 34 + 17 + 22 + 34 + 22 + 40
number_list = [9, 11, 22, 34, 17, 22, 34, 22, 40]
average = sum / 9
print(f"average: {average:.2f}")
sorted = statistics.median(number_list)
mode_number = statistics.mode(number_list)
print(f"median: {sorted}")
print(f"mode: {mode_number}")

number_list.append(34)

print(f"average: {average:.2f}")
sorted = statistics.median(number_list)
mode_number = statistics.mode(number_list)
print(f"median: {sorted}")
print(f"mode: {mode_number}")

