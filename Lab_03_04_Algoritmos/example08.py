"""
Cifrado César: El cifrado César es una técnica de cifrado simple en la que cada letra en
 el texto original se reemplaza por una letra un cierto número de posiciones más adelante en el alfabeto.
 Por ejemplo, con un desplazamiento de 1, "A" se reemplazaría por "B", "B" se convertiría en "C", etc. 
Escribe un programa que implemente el cifrado César para un mensaje y un desplazamiento dados."""
def cifrado_cesar(mensaje, desplazamiento):
    resultado = []
    for letra in mensaje:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            nueva_letra = chr((ord(letra) - base + desplazamiento) % 26 + base)
        else:
            nueva_letra = letra
        resultado.append(nueva_letra)
    return ''.join(resultado)

def run():

    mensaje_original = input("Introduce un texto : ")
    new_mensaje = mensaje_original.upper()
    desplazamiento = int(input("Ingrese un numero : "))
    mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)
    new_mensaje_cifrado = mensaje_cifrado.upper()
    print(" Mensaje original : {} ".format(new_mensaje))
    print("Mensaje cifrado: {} ".format(new_mensaje_cifrado))
    

if __name__ == "__main__":
    run()    


