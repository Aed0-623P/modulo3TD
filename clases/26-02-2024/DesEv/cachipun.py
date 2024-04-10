import random

while True:

    user = input("Piedra, Papel o Tijera?: ").lower()
    pc = random.choice(["Piedra", "Papel", "Tijera"]).lower()

    if user in ["piedra", "papel", "tijera"]:
    #input piedra
        if user == "piedra":
            if pc == "piedra":
                print("Tu Jugaste Piedra")
                print("Computador jugó Tijera")
                print("Ganaste!!")
            elif pc == "papel":
                print("Tu Jugaste Piedra")
                print("Computador jugó Papel")
                print("Perdiste!!")
            elif pc == "tijera":
                print("Tu Jugaste Piedra")
                print("Computador jugó piedra")
                print("Empataron!!")

        #input papel

        elif user == "papel":
            if pc == "tijera":
                print("Tu Jugaste Papel")
                print("Computador jugó Tijera")
                print("Perdiste!!")
            elif pc == "papel":
                print("Tu Jugaste Papel")
                print("Computador jugó Papel")
                print("Empataron!!")
            elif pc == "piedra":
                print("Tu Jugaste Papel")
                print("Computador jugó piedra")
                print("Ganaste!!")

        #input tijera

        elif user == "tijera":
            if pc == "piedra":
                print("Tu Jugaste Tijera")
                print("Computador jugó Piedra")
                print("Perdiste!!")
            elif pc == "papel":
                print("Tu Jugaste Tijera")
                print("Computador jugó Papel")
                print("Ganaste!!")
            elif pc == "tijera":
                print("Tu Jugaste Tijera")
                print("Computador jugó Tijera")
                print("Empataron!!")
    else:
        print("Elección inválida: Debe ser Piedra, Papel o Tijera.")        
    break
