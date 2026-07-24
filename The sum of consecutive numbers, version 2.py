limite = int(input("Limit: "))
somme = 1
nombre = 2
calcul = "1"

while somme < limite:
    somme += nombre
    calcul += f" + {nombre}"
    nombre += 1

print(f"The consecutive sum: {calcul} = {somme}")
