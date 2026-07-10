# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# Calcul du discriminant (b² - 4ac)
discriminant = (b ** 2) - (4 * a * c)

# Calcul des deux racines (le ± de la formule)
root1 = (-b + sqrt(discriminant)) / (2 * a)
root2 = (-b - sqrt(discriminant)) / (2 * a)

print(f"The roots are {root1} and {root2}")
