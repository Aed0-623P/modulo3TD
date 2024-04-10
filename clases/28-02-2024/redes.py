

a = [120, 50, 600, 30, 90, 10, 200, 0, 500]

filtro = ["bien" if i <= 90 else "mal" for i in a]

print(filtro)
