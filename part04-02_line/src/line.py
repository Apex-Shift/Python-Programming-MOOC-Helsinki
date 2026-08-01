def line(length, text):
    # On vérifie d'abord si la chaîne est vide
    if text == "":
        char = "*"
    else:
        # Si elle n'est pas vide, on prend le premier caractère
        char = text[0]
        
    print(char * length)

# Testing the function
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")