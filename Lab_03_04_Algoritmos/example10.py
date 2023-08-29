"""
Usa el método de formato de cadena para mostrar lo siguiente: 
radio = 10
area = 3.14 * radio ** 2
El área de un círculo con radio 10 es 314 metros cuadrados.
"""
import math
def run():
    radio = float(input("Ingrese el radio : "))
    area = math.pi*radio**2
    print("El area de un circulo con {} es : {:.2f}".format(radio,area))

if __name__ == "__main__":
    run()    