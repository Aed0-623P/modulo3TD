import sys
import random

lista = [1,2,3,4,5,6,7,8,9,0]

buscar = int(sys.argv[1])


for position, elemento in enumerate(lista):
    if elemento == buscar:
        print("elemento encontrado") == True
        break
    else:
        print(f"elemento {position} no encontrado")
