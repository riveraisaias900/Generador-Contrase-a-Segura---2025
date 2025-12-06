import random
import string

# Aquí se ingresa el mensaje de bienvenida al usuario
print("Hola, estás usando el siguiente programa que te ayudará a crear una contraseña segura.")
print("A continuación, agrega un número que definirá la longitud de la contraseña.")
print("El mínimo permitido es 8 dígitos.\n") 

# En esta seccion se le pedira al usuario cuantos digitos desea
n = int(input("¿Cuántos dígitos quieres para la contraseña? (mínimo 8): "))

def generar_contrasena(longitud):
    if longitud < 8:
        print("La longitud mínima es 8.")
        return None

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

print("Tu contraseña es:", generar_contrasena(n))