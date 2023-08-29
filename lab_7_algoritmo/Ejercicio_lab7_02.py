
""" 
A partir del archivo de datos proporcionado countries_data.py. Desarrollar lo siguiente:
a) ¿Cuál es el número total de idiomas en los datos?4ptos
b) Encuentra los diez idiomas más hablados a partir de los datos.4ptos
c) Encuentra los 10 países más poblados del mundo.4ptos
"""

# Importar el archivo countries_data.py
from Countries_data  import countries
def run():
    # a) ¿Cuál es el número total de idiomas en los datos?
    idiomas_totales = set()
    for pais in countries:
        idiomas_totales.update(pais["languages"])
        
    total_idiomas = len(idiomas_totales)
    print(f"a) El número total de idiomas en los datos es: {total_idiomas}")

    # b) Encuentra los diez idiomas más hablados a partir de los datos.
    idiomas_contador = {}
    for pais in countries:
        for idioma in pais["languages"]:
            idiomas_contador[idioma] = idiomas_contador.get(idioma, 0) + pais["population"]

    top_10_idiomas = sorted(idiomas_contador.items(), key=lambda x: x[1], reverse=True)[:10]
    print("b) Los diez idiomas más hablados son:")
    for idioma, poblacion in top_10_idiomas:
        print(f"{idioma}: {poblacion}")
        
    # c) Encuentra los 10 países más poblados del mundo.
    top_10_paises = sorted(countries, key=lambda x: x["population"], reverse=True)[:10]
    print("c) Los 10 países más poblados del mundo son:")
    for i in range(10):
        pais = top_10_paises[i]
        print(f"{i+1}. {pais['name']} - Población: {pais['population']}")
if __name__ == "__maain__":
    run()