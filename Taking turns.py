# Ask the user for a number
number = int(input("Please type in a number: "))

# Initialize two pointers at both ends of the range
left = 1
right = number

# Loop until the two pointers meet or cross each other
while left <= right:
    # Print the number from the lower end
    print(left)
    left += 1
    
    # Check if a number is still remaining at the upper end
    if left <= right:
        print(right)
        right -= 1
