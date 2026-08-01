# Ask the user to type in a sentence
sentence = input("Please type in a sentence: ")

# Split the sentence into a list of words based on spaces
words = sentence.split()

# Loop through each word and print its first character
for word in words:
    print(word[0])
