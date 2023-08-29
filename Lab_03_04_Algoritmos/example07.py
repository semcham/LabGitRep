"""
Inversión de palabras en una frase: Dada la frase "Aprendiendo Python con Edem".
 Escribe un programa que invierta el orden de las palabras en la frase, pero
  mantenga el orden de los caracteres en cada palabra.
 El resultado debería ser: "Edem con Python Aprendiendo"."""

def invertir_palabras(frase):
    palabra = frase.split()
    palabras_invertidas = palabra[::-1]
    resultado = " ".join(palabras_invertidas)
    return resultado

def run():
    frase = "Aprendiendo Python con Edem"
    frase_invertido = invertir_palabras(frase)
    print("La frase invertida es : ({})".format(frase_invertido))


if __name__ == "__main__":
    run()    