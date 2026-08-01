def line(length, text):
    # On garde ta fonction line d'origine
    if text == "":
        char = "*"
    else:
        char = text
    print(char * length)

def square_of_hashes(size):
    # Un carré a la même largeur et la même hauteur (size)
    for i in range(size):
        # On appelle line en lui donnant 'size' pour la largeur
        line(size, "#")

# Section de test
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)
