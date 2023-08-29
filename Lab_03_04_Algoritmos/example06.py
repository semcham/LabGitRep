"""
Contar caracteres y palabras: Dada la siguiente frase:
 "Estoy aprendiendo Python y me está gustando mucho. ¡Es genial!". 
 Escribe un programa en Python que cuente
 el número de palabras y de caracteres (incluyendo espacios y signos de puntuación)."""

def contar_caracteres_palabras(frase):

    palabras = frase.split()
    num_palabras = len(palabras)
    num_caracteres = len(frase)
    return num_palabras,num_caracteres


def run():

    frase ="Estoy aprendiendo Python y me está gustando mucho. ¡Es genial!"
    palabras,caracteres = contar_caracteres_palabras(frase)
    print("El numero de palabras es : {}".format(palabras))
    print("El numero de caracteres es : {}".format(caracteres))

if __name__ == "__main__":
    run()    



