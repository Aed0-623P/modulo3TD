prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')




prefijo = ['La', 'El', 'La', 'El']
frutas = ['harry', 'hermione', 'ron', 'draco']
colores = ['hufflepuff', 'slitherin', 'griffindor', 'nobody cares']

# Accessing specific elements in the print statement                 <----------
print(f'{prefijo[0]} {frutas[2]} es de color {colores[0]}')
#<------------------------------------------------------------>[] está indicando la ubicación