def chessboard(size):
    # Boucle pour chaque ligne (i va de 0 à size - 1)
    for i in range(size):
        row = ""
        # Boucle pour chaque caractère de la ligne (j va de 0 à size - 1)
        for j in range(size):
            # Si la somme des indices est paire, on met 1, sinon 0
            if (i + j) % 2 == 0:
                row += "1"
            else:
                row += "0"
        print(row)

# Testing the function
if __name__ == "__main__":
    chessboard(3)
