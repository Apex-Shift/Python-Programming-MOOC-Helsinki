def line(length, text):
    # On garde toujours ta fonction line d'origine intacte
    if text == "":
        char = "*"
    else:
        char = text
    print(char * length)

def square(size, character):
    # La boucle se répète autant de fois que la taille 'size'
    for i in range(size):
        # On passe la taille et le caractère personnalisé à la fonction line
        line(size, character)

# Section de test
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")
