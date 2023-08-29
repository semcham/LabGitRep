"""  
3) Generador de Contraseñas: Crea una función que genere contraseñas aleatorias. La función debe
aceptar parámetros como longitud de la contraseña y si debe incluir letras mayúsculas, minúsculas,
números y caracteres especiales. Utiliza funciones lambda para generar caracteres aleatorios y maneja
excepciones si se proporcionan parámetros inválidos.
"""

import random
import string

def generar_contraseña(longitud=12, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True):
    if not (incluir_mayusculas or incluir_minusculas or incluir_numeros or incluir_especiales):
        raise ValueError("Debes incluir al menos un tipo de carácter en la contraseña.")

    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    try:
        longitud = int(longitud)
        if longitud <= 0:
            raise ValueError("La longitud de la contraseña debe ser un número positivo.")
    except ValueError:
        raise ValueError("La longitud de la contraseña debe ser un número válido.")

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def run():
    try:
        contraseña = generar_contraseña(longitud=16, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True)
        print("La contraseña generada es : {}".format(contraseña))
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    run()

