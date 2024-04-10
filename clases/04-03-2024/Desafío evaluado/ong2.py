def calcular(**kwargs):
    for key, value in kwargs.items():
        if key == 'x':
            x = value
            x2 = fact_i(int(x))
            print(f"El factorial de {x} es {x2}")
        elif key == 'y':
            y = value
            y2 = prod_i(y)
            print(f"La productoria de {y} es {y2}")
        elif key == 'z':
            z = value
            z2 = fact_i(int(z))
            print(f"El factorial de {z} es {z2}")
        else:
            break
    return

def fact_i(x):
    y2 = 1
    x = int(x)
    while x > 1:
        y2 *= x
        x -= 1
    return y2

def prod_i(x):
    y = 1
    for num in x:
        num = int(num)
        y *= num
    return y


calcular(x=5, y=[3, 6, 4, 2, 8], z=6)


