with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()


unicos = set(texto)
contarchar = len(unicos)
print(f"El número de caracteres distintos es: {contarchar}")

tsplit = texto.split()
unicas = set(tsplit)
palabras = len(unicas)

# No sé si hay una discrepancia con el txt pero no logro hacer que me arroje 243 palabras

print(f"El número de palabras distintas es: {palabras}")
