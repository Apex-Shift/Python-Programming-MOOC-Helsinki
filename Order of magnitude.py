num = int(input("Pmease tupe in a number:"))
if num < 10 :
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")
if num < 100 and num > 10 :
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")
if num < 1000 and num > 100:
    print("This number is smaller than 1000")
    print("Thank you!")
if num > 1000:
    print("Thank you!")
