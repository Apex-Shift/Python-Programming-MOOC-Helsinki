def squared(text, size):
    index = 0
    # Boucle pour générer chaque ligne du carré
    for i in range(size):
        row = ""
        # Boucle pour ajouter chaque caractère de la ligne
        for j in range(size):
            row += text[index]
            # On passe au caractère suivant et on revient à 0 si on dépasse la fin
            index = (index + 1) % len(text)
        print(row)

# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
