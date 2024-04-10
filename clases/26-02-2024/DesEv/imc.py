import math


#inputs
w = float(input("Ingrese su peso en KG: "))
h = float(input("Ingrese su altura en centimetros: "))


#calculos
h2 = h/100
imc = w / (h2*h2)  #calcular imc normal
imc2 = "{:.2f}".format(imc)  #limitar el print del imc a dos decimales




if imc < 18.5:
    print("Su imc es ", imc2)
    print("La clasificación OMS es Bajo Peso")
elif imc >= 18.5 and imc < 25:
    print("Su imc es ", imc2)
    print("La clasificación OMS es Peso Adecuado")
elif imc >= 25 and imc < 30:
    print("Su imc es ", imc2)
    print("La clasificación OMS es Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Su imc es ", imc2)
    print("La clasificación OMS es Obesidad Grado I")
elif imc >= 35 and imc < 40:
    print("Su imc es ", imc2)
    print("La clasificación OMS es Obesidad Grado II")
elif imc >= 40:
    print("Su imc es ", imc2)
    print("La clasificación OMS es Obesidad Grado III")