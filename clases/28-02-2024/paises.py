

pais = ["mexico", "chile", "argentina"]
cant_usr = [70, 50, 55]

diccionario = {k:v for k,v in zip(pais, cant_usr)}
diccionario_filter = {k:v for k,v in diccionario.items() if v > 60}

print(diccionario)
print(diccionario_filter)