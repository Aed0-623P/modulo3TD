import math

r = float(input("Ingrese el radio en Kilómetros: "))
g = float(input("Ingrese la constante g: "))

r2 = r * 1000

a = float(g * r2)
b = 2 * a
root = math.sqrt(b)


print(f"La velocidad de Escape es {root:.1f} [m/s]")
