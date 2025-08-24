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


# METODOS EN LISTAS

# Añador nuevos elementos en tiempo de ejecucioón

courses.append("C++")  # agrega un elemento al final de la lista
courses.append("PHP")
courses.append("Laravel")

courses.insert(0, "Java")
courses.insert(4, "C#")
courses.insert(2, "MySQL")

# extender la lista atraves de otra lista
new_courses = ["React", "Nest"]
courses.extend(new_courses)

# BUSCAR SI UN VALOR SE ENCUENTRA EN EL LISTADO

found = "Python" in courses
found = courses.index("Flask")  # devuelve el indice del elemento

print(found)

# ELIMINAR ELEMENTOS DEL LISTADO

courses.remove("Ruby")
last_element = courses.pop()  # elimina el ultimo elemento
first_element = courses.pop(0)  # elimina el primer elemento y devulve el valor

print(last_element)
print(first_element)

# courses.clear()  # limpia la lista

print(courses)
print(len(courses))


# copy copiar litas
copia_lista = courses[:]
copia_lista = courses.copy()

print(copia_lista)
# reverse revirtir las lista

# reverse_list = courses[::-1]
courses.reverse()

# sort ordenarlos
courses.sort(reverse=True)  # ordena alfabeticamente modifica la lista
print(courses)

# MATRIZ
# Las listas no son mas que colecciones que no permite almacenar defierente tipos de datos
# se puede trabajar con n dimenciones
# 3x3
matrix = [
    [1, 2, 3],  # indice 0
    [4, 5, 6],  # indice 1
    [7, 8, 9]   # indice 2
]

print(matrix)

print(
    matrix[1][1]
)
