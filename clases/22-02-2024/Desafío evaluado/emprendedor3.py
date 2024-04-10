p = float(input("Precio subscripción, ingrese por favor solo en números: "))
u = float(input("Número de usuarios, ingrese por favor solo en números: "))
gt = float(input("Ingrese el Gasto Total, ingrese por favor solo en números: "))
ut_a = float(input("Utilidades año anterior, ingrese por favor solo en números: "))
# ut_a utilidad total anual año anterior

ut = (p * u) - gt  # calculo utilidad mensual actual
ut_a2 = ut_a / 12

fin = ut / ut_a2  # calculo la comparación de utilidades


print(
    f"La razón entre utilidades actuales y las del año anterior es: {fin:.2f}"
)  # print final y dos decimales
