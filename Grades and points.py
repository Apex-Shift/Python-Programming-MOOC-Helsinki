points = int(input("How many points [0-100]:"))
if points < 0:
    print("Grade: impossible!")

if points >= 0 and points <= 49:
    print("Grade: fail")

if points >= 50 and points <= 59:
    print("Grade: 1")

if points >= 60 and points <= 69:
    print("Grade: 2")
if points >= 70 and points <= 79:
    print("Grade: 3")
if points >= 80 and points <= 89:
    print("Grade: 4")
if points >= 90 and points <= 100:
    print("Grade: 5")
if points > 100:
    print("Grade : impossible!")


