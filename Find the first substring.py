text = input("Please type in a string: ")
character = input("Please type in a character: ")

index = text.find(character)

if index != -1 and index + 3 <= len(text):
    print(text[index:index+3])
