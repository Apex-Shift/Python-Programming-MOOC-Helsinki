limite = int(input("Upper limit: "))
base = int(input("Base: "))
nombre = 1

while nombre <= limite:
    print(nombre)
    nombre *= base  # Multiplie par la base choisie au lieu de 2
