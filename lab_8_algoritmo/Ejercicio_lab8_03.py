
""" 
3) Ejercicio Complejo: Generador de Contraseñas Seguras
Descripción: Vamos a crear un generador de contraseñas seguras utilizando los conceptos que hemos aprendido hasta ahora, incluyendo funciones, módulos y control de flujo. La idea es que el programa genere una contraseña aleatoria con una longitud específica y asegure que cumple con ciertos requisitos de seguridad.
a) Requisitos de seguridad de la contraseña:
b) La contraseña debe tener al menos 8 caracteres.
c) Debe incluir al menos una letra mayúscula y una letra minúscula.
d) Debe contener al menos un número.
e) Debe contener al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
"""


# Importar los módulos necesarios
import string, random
# Definir una función que genera un carácter aleatorio de un conjunto específico
def generarCaractRan():
 # Crear un diccionario que mapea números a diferentes tipos de caracteres aleatorios
    caracterAleatorio = {
        1: random.choice(string.ascii_uppercase),# Letra mayúscula aleatoria
        2: random.choice(string.ascii_lowercase),# Letra minúscula aleatoria
        3: random.choice(string.digits), # Dígito aleatorio
        4: random.choice(string.punctuation)# Carácter de puntuación aleatorio
    }
    return caracterAleatorio

def generarContraseña8dig():

    contraseña = ""  # Inicializar una cadena vacía para almacenar la contraseña
    numerosRandom = random.sample([1, 2, 3, 4], 4) # Se eligen cuatro números aleatorios del 1 al 4 sin repetición
# Generar la contraseña combinando caracteres aleatorios
    for i in range(4):
        # Agregar un carácter aleatorio del tipo especificado por numerosRandom[i]
        # Agregar otro carácter aleatorio de cualquier tipo (1 al 4)
        contraseña += generarCaractRan().get(numerosRandom[i]) + generarCaractRan().get(random.randint(1, 4))

    return contraseña

def run():
    print(generarContraseña8dig())#imprimimos la  contraseña


if __name__ == "__main__":
    run()



