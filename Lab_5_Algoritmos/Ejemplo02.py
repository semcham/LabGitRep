""" 
“Soy profesor y me encanta inspirar y enseñar a la gente”. 
¿Cuántas palabras únicas se han utilizado en la
frase? Usa los métodos de split y sets para obtener las palabras únicas. (4pto)
"""

def run():

    frase = "Soy profesor y me encanta inspirar y enseñar a la gente"
    new_frase = frase.split()
    print(new_frase)

    palabras_unicas = set(new_frase)
    print("palabras unicas : {} ".format(palabras_unicas))
    longitud_palabras_unicas = len(palabras_unicas)
    print("cantidad de palabras unicas: {}".format(longitud_palabras_unicas))


if __name__ == "__main__":
    run()