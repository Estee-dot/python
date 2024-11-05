change = int(input("enter the change: "))

quarter = change // 25
remain = change % 25
dimes = remain // 10
remain_one = remain % 10
pennies = remain_one


print(f"quarter: {quarter}\ndimes: {dimes}\npennies: {pennies}")

