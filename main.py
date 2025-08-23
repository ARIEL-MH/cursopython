# Esto en un comentario

print('Hola Mundo, desde un script en Python.')
'''
    Esto es un comentario de mas líneas
    Dejar anotaciones para los desarrolladores
'''
"""
    Esto es un comentario con triples comillas
"""
# Variables

"""
Python es un lenguaje de tipado dianmico
<variable> = <valor>
"""

name = 'Eduardo'
age = 10

print(age)
# Conocer el tipo de la variable
print(type(age))

# Covencion para variables con snake_case
# Crear variables con nombre descriptivo
es_adminstrado = False
print(es_adminstrado)


# Strings "" - ''
# Integers
# Floats
# Booleans True / False

# No existe diferencia al crear con "" o '' sola al usarlas
first_name = "C'o'dy"  # lenguaje de tipado dianmico el tipo se infiere
last_name = 'F"a"cilito'

print(first_name)
print(last_name)

print(type(first_name))
print(type(last_name))


age = -13
number = 100_000_0000  # Python permite usar _ para mejorar la lectura de números grandes
print(age)
print(type(age))

pi = 3.1416  # variable de tipo float

print(pi)
print(type(pi))

# los booleanos verdadero(True) o falso(False)
is_active = False
print(is_active)
print(type(is_active))
