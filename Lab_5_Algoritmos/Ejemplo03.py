""" 
Considera tres listas de números enteros, una con números del 1 al 10, otra con números del 5 al 15, y la
última con números del 10 al 20. (5ptos)
a. Convierte las listas en conjuntos.
b. Encuentra el conjunto de todos los números que están presentes en las tres listas.
c. Encuentra el conjunto de todos los números que están presentes en al menos una de las listas.
d. Encuentra el conjunto de todos los números que están presentes en la primera lista, pero no en la última.
e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla.
"""
def run():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = [5,6,7,8,9,10,11,12,13,14,15]
    list3 = [10,11,12,13,14,15,16,17,18,19,20]
    # a) convierte las listas en conjuntos
    conjunto1 = set(list1)
    conjunto2 = set(list2)
    conjunto3 = set(list3)
    # b) Encuentra el conjunto de todos los números que están presentes en las tres listas.
    
    conjunto_comun = conjunto1.intersection(conjunto2,conjunto3)
    # c. Encuentra el conjunto de todos los números que están presentes en al menos una de las listas.
    conjunto_total = conjunto1.union(conjunto2,conjunto3)
    # d. Encuentra el conjunto de todos los números que están presentes en la primera lista, pero no en la última.
    conjuto_diferencia = conjunto1.difference(conjunto2,conjunto3)
    # e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla.
    tupla_comun = tuple(conjunto_comun)
    tupla_total = tuple(conjunto_total)
    tupla_diferencia = tuple(conjuto_diferencia)
    suma_primer_ultimo_comun = tupla_comun[0]+tupla_comun[-1]
    suma_primer_ultimo_total = tupla_total[0]+tupla_total[-1]
    suma_primer_ultimo_diferencia = tupla_diferencia[0]+tupla_diferencia[-1]
    # ahora imprimimos los resultados obtenidos
    print(" a) conjuntos :")
    print("conjunto 1 : {} ".format(conjunto1))
    print("conjunto 2 : {} ".format(conjunto2))
    print("conjunto 3 : {} ".format(conjunto3))
    # b)
    print("El conjunto comun es : {}".format(conjunto_comun))
    # c)
    print("El conjunto total es : {}".format(conjunto_total))
    # d)
    print("El conjunto diferencia es : {}".format(conjuto_diferencia))
    # e)
    print("La suma del primer y del ultimo elemento de la tupla comun es : {}".format(suma_primer_ultimo_comun))
    print("La suma del primer y del ultimo elemento de la tupla total es : {}".format(suma_primer_ultimo_total))
    print("La suma del primer y del ultimo elemeto de la tupla diferencia es : {}".format(suma_primer_ultimo_diferencia))


if __name__ == "__main__":
    run()