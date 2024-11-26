def even_number(integer):

    sum = 0
    for count in range(1, integer +1 , 2):
           sum = sum + 1
           return sum

integer = int(input("Give a number: "))
print(even_number(integer))