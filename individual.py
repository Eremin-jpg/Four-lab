from math import *

a = float(input("Enter the length of the first base: "))
b = float(input("Enter the length of the second base: "))
h = float(input("Enter the height: "))

side = sqrt(((a - b) / 2) ** 2 + h ** 2)
perimeter = a + b + 2 * side

print(f"Perimeter: {perimeter:.2f}")