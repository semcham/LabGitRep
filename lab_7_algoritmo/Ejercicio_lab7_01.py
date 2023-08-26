
""" 
1) Aquí tenemos un diccionario de una persona. ¡Siéntete libre de modificarlo!
persona = {
'first_name': 'Edem',
'last_name': 'Terraza',
'age': 31,
'country': 'Peru',
'is_married': True, #
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}
a) Comprueba si el diccionario de la persona tiene la clave de habilidades; si es así, imprime 
la habilidad del medio en la lista de habilidades. 2.5ptos
b) Comprueba si el diccionario de la persona tiene la clave de habilidades; si es así, verifica 
si la persona tiene la habilidad 'Python' e imprime el resultado. 2.5ptos
c) Si las habilidades de una persona tienen solo JavaScript y React, imprime 
('Él es un desarrollador frontend'), si las habilidades de la persona tienen Node, Python, MongoDB, 
imprime ('Él es un desarrollador backend'), si las habilidades de la persona tienen React, Node y MongoDB, 
imprime ('Él es un desarrollador fullstack'), de lo contrario imprime ('título desconocido') 
- ¡para obtener resultados más precisos, se pueden anidar más condiciones! 3ptos
"""


def run():
        # Diccionario de la persona
    persona = {
        'first_name': 'Edem',
        'last_name': 'Terraza',
        'age': 31,
        'country': 'Peru',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }

    # a) Comprobar si el diccionario de la persona tiene la clave 'skills'
    if 'skills' in persona:
        skills = persona['skills']
        if len(skills) >= 3:
            print("La habilidad del medio en la lista de habilidades es:", skills[len(skills) // 2])
        else:
            print("La lista de habilidades no tiene suficientes elementos para encontrar una habilidad del medio.")

    # b) Comprobar si el diccionario de la persona tiene la clave 'skills' y si contiene la habilidad 'Python'
    if 'skills' in persona and 'Python' in persona['skills']:
        print("La persona tiene la habilidad 'Python'.")
    else:
        print("La persona no tiene la habilidad 'Python'.")

    # c) Determinar el título del desarrollador
    if 'skills' in persona:
        skills = persona['skills']
        if 'JavaScript' in skills and 'React' in skills in skills:
            print("Él es un desarrollador frontend.")
        elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
            print("Él es un desarrollador backend.")
        elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
            print("Él es un desarrollador fullstack.")
        else:
            print("Título desconocido.")
    else:
        print("El diccionario de la persona no contiene habilidades.")


if __name__ == "__main__":
    run()