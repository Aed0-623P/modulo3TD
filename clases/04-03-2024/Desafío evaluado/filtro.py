import sys

precios = {
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de Video": 1500000,
}

def filtrado(diccionario, umbral, v):
    if "mayor" in v:
        mayores = ", ".join([k for k, v in diccionario.items() if v > umbral])
        return f"los productos mayores al umbral son: {mayores}"
    else:
        menores = ", ".join([k for k, v in diccionario.items() if v < umbral])
        return f"los productos menores al umbral son: {menores}"

umbral = int(sys.argv[1])
v = sys.argv[2] if len(sys.argv) > 2 else "mayor"
resultado = filtrado(precios, umbral, v)
print(resultado)