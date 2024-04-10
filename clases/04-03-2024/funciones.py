import math


def media(lista):
    return sum(lista) / len(lista)


def sdd(lista, media):
    diff = [(elemento - media) ** 2 for elemento in lista]
    return math.sqrt(sum(diff) / (len(lista) - 1))


def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estandarizada = [(valor - m) / sd for valor in lista]
    return m, sd, lista_estandarizada


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

m, desv_st, l_e = resultado(lista)
print("la media es: ", m)
print("la desviación estandar es:", desv_st)
print("la lista estandariza es: ", l_e)
