word = input("Word: ")

print("*" * 30)

spaces = 28 - len(word)
left_spaces = spaces // 2
right_spaces = spaces - left_spaces

print("*" + " " * left_spaces + word + " " * right_spaces + "*")
print("*" * 30)
