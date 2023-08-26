"""
1) Ve a la carpeta de datos y accede al archivo countries-data.py.}
a) Crea una función llamada los idiomas más hablados en el mundo. Debería devolver los 10 o 20 idiomas más hablados en el mundo en orden descendente.
b) Crea una función llamada los países más poblados. Debería devolver los 10 o 20 países más poblados en orden descendente.
"""



# Importamos los datos desde Countries_data.py
from Countries_data import countries

# Definemos la función para obtener los idiomas más hablados en el mundo
def los_idiomas_mas_hablados(n=10 ):
    # Ordenamos los países por el número de hablantes de idiomas en orden descendente
    idiomas_por_poblacion = sorted(countries, key=lambda x: x['population'], reverse=True)
    # Extraemos los n idiomas más hablados
    idiomas_mas_hablados = [pais['languages'] for pais in idiomas_por_poblacion[:n]]
    return idiomas_mas_hablados
# Definemos la función para obtener los países más poblados en el mundo
def los_paises_mas_poblados(n=10):
    # Ordenamos los países por población en orden descendente
    paises_mas_poblados = sorted(countries, key=lambda x: x['population'], reverse=True)[:n]

    return paises_mas_poblados
def run():
    # Obtenemos los 10 idiomas más hablados en el mundo
    idiomas = los_idiomas_mas_hablados(10)
    print("Los 10 idiomas más hablados en el mundo son:")
    for idioma in idiomas:
        print(idioma)

    # Obtenemos los 10 países más poblados en el mundo
    paises = los_paises_mas_poblados(10)
    print("\nLos 10 países más poblados en el mundo son:")
    for pais in paises:
        print(f"{pais['name']} - Población: {pais['population']}")

if __name__ == "__main__":
    run()