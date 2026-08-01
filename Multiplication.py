# Ask the user for a positive integer
number = int(input("Please type in a number: "))

# Nested loops to generate the multiplication table up to the given number
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f"{i} x {j} = {i * j}")
