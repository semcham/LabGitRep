"""
Encuentra la longitud del texto python, convierte el valor
a float y luego conviértelo a string (1pto)
"""


def run():
    texto = "python"
    longitud  = len(texto)
    longitud_float = float(longitud)
    longitud_string = str(longitud_float)
    print(longitud)
    print(longitud_float)
    print(longitud_string)


if __name__ == "__main__":
    run()    