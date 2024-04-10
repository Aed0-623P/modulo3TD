from string import ascii_lowercase
import getpass
import string

clave = getpass.getpass("entre la contraseña solo en letras")

checks = 0

for i in clave:
    for i2 in string.ascii_lowercase:
        if i == i2:
            checks += 1
            break
        else:
            checks +=1

print(f"La contraseña fue forzada en: {checks}")


