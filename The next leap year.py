start_year = int(input("Year: "))
year = start_year + 1

while True:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"The next leap year after {start_year} is {year}")
        break
    year += 1
