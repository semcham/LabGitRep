

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

"""  
3)'sys.stdin', 'sys.stdout', y 'sys.stderr': Estas son variables que representan las corrientes de entrada estándar, salida
 estándar y salida de errores estándar, respectivamente. Puedes redirigir estas corrientes 
 si es necesario para cambiar dónde se imprimen los datos.
 """

"""  
4)'sys.platform': Esta variable proporciona información sobre la plataforma subyacente en la que 
se ejecuta Python, como "win32" para Windows, "linux" para Linux, etc.
ejemplo:
"""
import sys
print("Plataforma actual:", sys.platform)

"""
5)'sys.version': Esta variable contiene una cadena que describe la versión de Python que se está ejecutando.
ejemplo:
"""
import sys
print("Versión de Python:", sys.version)

"""
6)'sys.exit()': Esta función se utiliza para salir de un programa Python con un código 
de estado específico. Por ejemplo, sys.exit(0)indica una salida 
exitosa, mientras que sys.exit(1)indica una salida con un error.
ejemplo:
"""
import sys

if algo_salio_mal:
    sys.exit(1)  # Salir con un código de error
else:
    sys.exit(0)  # Salir con éxito

"""
7)'sys.getsizeof(object)': Esta función devuelve el tamaño en bytes de un objeto en memoria.
ejemplo:
"""
import sys
my_list = [1, 2, 3, 4, 5]
print("Tamaño de la lista en bytes:", sys.getsizeof(my_list))
"""
8)'sys.maxsize': Esta variable proporciona el valor máximo que puede tener un objeto de tipo entero en la plataforma actual.
ejemplo:
"""
import sys
print("Valor máximo para enteros:", sys.maxsize)
