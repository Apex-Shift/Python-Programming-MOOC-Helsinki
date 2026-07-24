text = input("Please type in a string: ")
character = input("Please type in a character: ")

index = 0
while index < len(text):
    if text[index] == character:
        if index + 3 <= len(text):
            print(text[index:index+3])
    index += 1
