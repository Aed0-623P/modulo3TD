import random

pool = [n for n in range(1, 42)]

posiciones = [
    "primer numero",
    "segundo numero",
    "tercer numero",
    "cuarto numero",
    "quinto numero",
    "sexto numero",
    "comodin",
]


def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f"el {posicion} es {elegido}")


for posicion in posiciones:
    sacar_numero(posicion)
    print(pool)


print("sorteo terminado")
