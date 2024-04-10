import getpass
password = getpass.getpass("Ingrese la clave secreta: ")
while password != "hola mundo":
 password = getpass.getpass("La clave secreta no es correcta. Intenta otra vez.")