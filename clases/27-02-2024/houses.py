dicc = {
    "a": ["Hermione", "Ron", "Harry", "Draco"],
    "b": ["Hufflepuff", "griffindor", "slithering", "nobody cares"]
}

for key, value in dicc.items():
    print(f"{value[2]} is {key}")

#asignar key a la casa y value al nombre del weas
    #para imprimir de distintas listas hay que pedir dos print separados

for key, value in dicc.items():
    print(f"{value[2]} is {key}")
    print(f"{value[3]} is {key}")

#printea value value y key key, no queria hacer eso, what do boss
    #referir a funcion zip()