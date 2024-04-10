valores = [0,4,5,6,7,8,9]
divisibles = []
nodiv = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisibles')
    else:
        nodiv.append('No Divisible')