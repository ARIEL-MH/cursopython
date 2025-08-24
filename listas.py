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

courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"]
number = [1, 2, 3, 4, 5]  # lista de solo números con 5 elementos


# utilizando indice se puede modificar la colección o ver el valor del elemento
# print(courses[0])  # Imprime Python

# VER ELEMENTOS

last_index = len(courses) - 1
value = courses[last_index]  # ver el ultimo elemento

value = courses[-3]  # ver el ultimo elemento con numeros negativos

print(value)

# print(courses)
# print(number)


# ACTUALIZAR ELEMENTOS
courses[0] = "JavaScript"  # remplaza Python por JavaScript
courses[-1] = "PostgreSQL"  # remplaza MongoDB por PostgreSQL

print(courses)


# SUBLISTAS

#  Slicing    [start:end:skips]
new_list = courses[0:3]  # desde el indice 0 hasta el 2
new_list = courses[:3]  # python reconoce que inicaremos desde el indice 0
new_list = courses[2:]  # desde el indice 2 hasta el final

courses_copy = courses[:]  # copia toda la lista

courses_copy = courses[::2]  # copia con saltos de dos en dos
courses_copy = courses[::-1]  # invertir la lista

# new_list = [
#     courses[0],
#     courses[1],
#     courses[2]
# ]

print(new_list)
print(courses_copy)
