"""  
1) La siguiente es una lista de las edades de 10 estudiantes:
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] (4ptos)
a. Ordena la lista y encuentra la edad mínima y máxima
b. Añade de nuevo la edad mínima y máxima a la lista
c. Encuentra la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
d. Encuentra la edad promedio (suma de todos los elementos divididos por su número)
e. Encuentra el rango de las edades (máximo menos mínimo)
f. Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs()
"""
def run():
    edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    # a. Ordena la lista y encuentra la edad mínima y máxima
    edades_ordenadas = sorted(edades)
    edad_minima = edades_ordenadas[0]
    edad_maxima = edades_ordenadas[-1]

    # b. Añade de nuevo la edad mínima y máxima a la lista
    edades.append(edad_minima)
    edades.append(edad_maxima)

    # c. Encuentra la edad mediana
    n = len(edades_ordenadas)
    if n % 2 == 1:
        mediana = edades_ordenadas[n // 2]
    else:
        mediana = (edades_ordenadas[n // 2 - 1] + edades_ordenadas[n // 2]) / 2

    # d. Encuentra la edad promedio
    promedio = sum(edades) / len(edades)

    # e. Encuentra el rango de las edades
    rango = edad_maxima - edad_minima

    # f. Compara el valor de (mínimo - promedio) y (máximo - promedio) usando abs()
    diferencia_minimo = abs(edad_minima - promedio)
    diferencia_maximo = abs(edad_maxima - promedio)

    # Imprimir resultados
    print("Edad mínima:", edad_minima)
    print("Edad máxima:", edad_maxima)
    print("Lista de edades con mínima y máxima añadidas:", edades)
    print("Mediana de las edades:", mediana)
    print("Edad promedio:", promedio)
    print("Rango de las edades:", rango)
    print("Diferencia entre mínimo y promedio:", diferencia_minimo)
    print("Diferencia entre máximo y promedio:", diferencia_maximo)
if __name__ == "__main__":
    run()