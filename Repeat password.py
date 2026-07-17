password = input("Password: ")

while True:
    repeat = input("Repeat password: ")
    if password == repeat:
        print("User account created!")
        break
    else:
        print("They do not match!")
