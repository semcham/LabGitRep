"""
Palíndromos: Un palíndromo es una palabra, frase, número u otro tipo de unidad que se puede
leer igual hacia adelante que hacia atrás 
(ignorando espacios, acentos y signos de puntuación), como "anilina" o "reconocer". 
Escribe un programa en Python que detecte si una frase dada es un palíndromo.
"""
import re
def es_palindromo(frase):

    frase_limpia = re.sub(r'[^a-zA-Z]', '', frase).lower()
    return frase_limpia == frase_limpia[::-1]

def run():
    frase = input("Introduce una frase : ")
    new_frase = frase.upper()
    if es_palindromo(frase):
        print("La '{}' es un palindromo.".format(new_frase))
    else:
        print("La '{}' no es un palindromo.".format(new_frase))

if __name__ == "__main__":
    run()    