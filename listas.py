"""
Estructura para crear listas
<variable> = []

hay que trabajar con listas que alamacen un solo tipo de dato
trabajar con listas homogéneas
"""

# my_list = ["String", 10, 3.14, True, [1, 2, 3]]
# print(type(list))


# indices  0            1        2        3        4
# indices  -5            -4        -3        -2        -1

curses = ["Python", "Django", "Flask", "Ruby", "MongoDB"]
number = [1, 2, 3, 4, 5]  # lista de solo números con 5 elementos


# utilizando indice se puede modificar la colección o ver el valor del elemento
# print(curses[0])  # Imprime Python

# VER ELEMENTOS

last_index = len(curses) - 1
value = curses[last_index]  # ver el ultimo elemento

value = curses[-3]  # ver el ultimo elemento con numeros negativos

print(value)

# print(curses)
# print(number)


# ACTUALIZAR ELEMENTOS
curses[0] = "JavaScript"  # remplaza Python por JavaScript
curses[-1] = "PostgreSQL"  # remplaza MongoDB por PostgreSQL

print(curses)
