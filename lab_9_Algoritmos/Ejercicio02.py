

"""  
2) Calculadora Simple: Crea una calculadora simple que pueda realizar operaciones básicas como suma, resta, multiplicación
y división. La calculadora debe aceptar dos números del usuario y el tipo de operación que desea realizar.
Maneja excepciones en caso de errores de entrada.
"""
def suma(n1,n2):
    return n1+n2
def resta(n1,n2):
    return n1-n2
def multiplicación(n1,n2):
    return n1*n2
def división(n1,n2):
    return n1/n2

def run():
    try:
        n1 = int(input("Ingrese el primer numero entero :  "))
        n2 = int(input("Ingrese el segundo numero entero : "))
        opc = input("Ingrese una opcion (+,-,*,/) : ")
        if opc == "+":
            Suma = suma(n1,n2)
            print("La suma es : {}".format(Suma))
        elif opc == "-":
            Resta = resta(n1,n2)
            print(" La resta  es : {}".format(Resta))
        elif opc == "*":
            multiplicar = multiplicación(n1,n2)
            print("La multiplicacion es : {}".format(multiplicar))
        elif opc == "/":
            dividir = división(n1,n2)
            print("la division es : {}".format(dividir))
        else:
            print("Introduce una opcion valida.")
    except ValueError:
        print("ERROR .El valor ingresaso no es valido")
    except ZeroDivisionError:
        print("No se puede dividr entre cero.")
    except TypeError:
        print("EL tipo de dato es incorrecto.")
if __name__ == "__main__":
    run()