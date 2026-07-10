hr_wage = float(input("Houly wage:"))
hrs_worked = int(input("Hours worked:"))
day = input("Day of the week:")

daily_wage = hr_wage * hrs_worked

if day != "Sunday":
   print("Daily wages:",daily_wage,"euros")
else:
    print("Daily wages:",daily_wage * 2,"euros" )
