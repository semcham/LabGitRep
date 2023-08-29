"""  
1) Conversor de Temperatura: Escribe un programa que convierta entre Celsius y Fahrenheit. El
programa debe permitir al usuario ingresar una temperatura y la unidad en la que está (C o F). Luego,
realiza la conversión y muestra el resultado. Utiliza funciones y control de flujo para realizar las
conversiones y manejar excepciones en caso de entradas incorrectas.
"""
def grados_celcius_a_Fahrenheit(celcius):
    grado_Fahrenheit = (celcius*(9/5))+32
    return grado_Fahrenheit
def grados_Fahrenheit_a_celcius(Fahrenheit):
    grado_celcius =(Fahrenheit-32)*(5/9)
    return grado_celcius
def run():
    try:
        temperatura = float(input(" Ingrese la tempertura : "))
        unidad = input("Ingrese la opcion (C o F) : ").upper()
        if unidad == "C":
            grado_celcius = grados_Fahrenheit_a_celcius(temperatura)
            print("Los grados Fahrenheit({}) en celcius es : {}".format(temperatura, grado_celcius))
        elif unidad == "F":
            grados_Fahrenheit = grados_celcius_a_Fahrenheit(temperatura)
            print("los grados celcius({}) en Fahrenheit es : {}".format(temperatura, grados_Fahrenheit))
        else:
            print("Introduce nuevamente una de las dos opciones ")
    except ValueError:
        print("El valor ingresado es incorrecto. Por favor ingrse una opcion valida.")


if __name__ == "__main__":
    run()


