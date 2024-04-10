lista = [0,1,2,3,4,5,6,7,8,9,10]

for numero1 in lista:
    print(f"\ntabla del {numero1}:------------------\n")
    for numero2 in lista:
        print(f"{numero1}*{numero2} = {numero1 * numero2}")