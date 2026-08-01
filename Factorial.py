while True:
    # Ask the user for an integer
    number = int(input("Please type in a number: "))
    
    # If the number is 0 or below, end the execution
    if number <= 0:
        print("Thanks and bye!")
        break
    
    # Calculate the factorial
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
        
    # Print the result
    print(f"The factorial of the number {number} is {factorial}")
