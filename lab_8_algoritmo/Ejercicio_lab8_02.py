

#Investigar el módulo sys

""" 
El módulo syses un módulo incorporado en Python que proporciona acceso a variables y 
funciones que interactúan con el intérprete de Python y el sistema operativo subyacente. 
Puedes usar el módulo syspara realizar tareas como argumentos de línea de comandos, acceder a rutas
de búsqueda para módulos, controlar el flujo de entrada y salida estándar, y más
 """
"""  
1)'sys.argv': Esta es una lista que contiene los argumentos de línea de comandos pasados ​​al 
script Python. El primer elemento ( sys.argv[0]) generalmente es el nombre del script en sí.
 """
 
import sys
print("Nombre del script:", sys.argv[0])
print("Argumentos de línea de comandos:", sys.argv[1:])

""" 
2)'sys.path': Es una lista que contiene las rutas de búsqueda para módulos. Python busca módulos en estas rutas 
cuando intentas importarlos. Puedes modificar esta lista para agregar rutas personalizadas.
ejemplo:
"""
import sys
print("Rutas de búsqueda para módulos:", sys.path)
