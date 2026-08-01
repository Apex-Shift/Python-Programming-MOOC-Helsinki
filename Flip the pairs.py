# Ask the user for a number
number = int(input("Please type in a number: "))

# Start counting from 1
i = 1

# Loop through the numbers by steps of 2 to handle pairs
while i <= number:
    # If the second number of the pair is within the limit, print it first
    if i + 1 <= number:
        print(i + 1)
        print(i)
    else:
        # If the number is odd and we reached the last single number
        print(i)
    
    # Move to the next pair
    i += 2
