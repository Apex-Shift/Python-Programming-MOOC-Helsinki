def line(length, text):
    # On garde ta fonction précédente intacte
    if text == "":
        char = "*"
    else:
        char = text
    print(char * length)

def box_of_hashes(height):
    # On fait une boucle qui se répète autant de fois que la hauteur demandée
    for i in range(height):
        # On appelle la fonction line : largeur de 10, avec le caractère "#"
        line(10, "#")

# Section de test (TMC l'ignorera lors de la soumission)
if __name__ == "__main__":
    box_of_hashes(5)
