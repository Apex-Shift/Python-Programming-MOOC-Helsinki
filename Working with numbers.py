print("Please type in integer numbers. Type in 0 to finish.")

count = 0
total_sum = 0
positives = 0
negatives = 0

while True:
    number = int(input("Number: "))
    
    if number == 0:
        break
        
    count += 1
    total_sum += number
    
    if number > 0:
        positives += 1
    else:
        negatives += 1

mean = total_sum / count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total_sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")
