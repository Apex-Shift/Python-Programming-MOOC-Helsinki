# 1. Ask the user for two strings
string_1 = input("Please type in string 1: ")
string_2 = input("Please type in string 2: ")

# 2. Compare the lengths using len()
if len(string_1) > len(string_2):
    print(string_1 + " is longer")
elif len(string_2) > len(string_1):
    print(string_2 + " is longer")
else:
    print("The strings are equally long")
