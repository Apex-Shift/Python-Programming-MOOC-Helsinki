def hash_square(length):
    # Boucle pour imprimer chaque ligne du carré
    for i in range(length):
        print("#" * length)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(3)
    print()
    hash_square(5)
