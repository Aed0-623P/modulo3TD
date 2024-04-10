p = float(input("Precio subscripción, ingrese por favor solo en números: "))
u = float(input("Número de usuarios, ingrese por favor solo en números: "))
u2 = float(input("Número de usuarios premium, ingrese por favor solo en números: "))
gt = float(input("Ingrese el Gasto Total, ingrese por favor solo en números: "))

ut = (p * u) + (p * (u2 * 1.5)) - gt  # calculo utilidades mensual + usuario premium

print(ut)
