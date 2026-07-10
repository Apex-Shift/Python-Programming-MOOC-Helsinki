eating_freq = int(input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

week_caf_lun = lunch_price * eating_freq
weekly_exp = groceries + week_caf_lun
daily_exp = weekly_exp / 7

print("Average food expenditure:")
print("Daily:",daily_exp,"euros")
print("Weekly:",weekly_exp,"euros")
