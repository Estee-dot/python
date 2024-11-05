principal = 1000
rate = 7 / 100
year = 0

annual_rate = 0

for year in range(1, 31):
    annual_rate = principal * ((1 + rate) ** year)
    print(annual_rate)
    print()