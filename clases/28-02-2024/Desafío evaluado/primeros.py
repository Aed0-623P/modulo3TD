innit = input("Responde a estímulos? ").lower()
if innit == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
elif innit == "no":
    print("Abrir la vía aérea")
    resp = input("¿Respira? ").lower()
    if resp == "si":
        print("Permitirle posición de suficiente ventilación")
    elif resp == "no":
        print("Administrar 5 ventilaciones y llamar a la ambulancia")
        while True:
            vida = input("¿Signos de vida? ").lower()
            if vida == "no":
                print(
                    "Administrar compresiones torácicas hasta que llegue la ambulancia"
                )
                ambu = input("¿Llegó la ambulancia? ").lower()
                if ambu == "no":
                    continue
                else:
                    break
            elif vida == "si":
                print("Reevaluar la espera de la ambulancia")
                ambu = input("¿Llegó la ambulancia? ").lower()
                if ambu == "no":
                    continue
                else:
                    break
