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


"""
En python las contantes no existen
CON MAYUSCULAS ES CONSTANTE
"""
VERSION = 3.14
print(VERSION)


# NUMEROS ENTEROS NUMEROS POSITIVOS O NEGATIVOS
number = 10
result = number / 10  # se obtiene siempre float
result = number // 10  # se obtiene siempre resultado entero

print("El resultado es:", result)

# OPERADORES RELACIONALES se obtiene (True/False)
# se usan para comparar numeros
# ==, !=, >, <, >=, <=

number_one = 10
number_two = 20

result = number_one < number_two  # False
print("El resultado de la comparacion es:", result)
print(type(result))

# OPERADORES LÓGICOS
# se usan para combinar expresiones booleanas
# and, or, not

number_one = 10
number_two = 20
# Todos los valores deben ser True para que sea verdadero en and
# Con or por lo menos debe existir un verdadero para que sea verdadero
# not se niega la expresion
result = (
    True
    and True
    and number_one != number_two
    and number_one < 100
    and number_two > 200
)
print(result)


# PARA PEDIR VALORES POR TECLADO

# por defecto toma el valor como string
# full_name = input('Ingresa tu nombre: ')
# print('Hola', full_name)


# EJEMPLO DE PROGRAMA
nombre_completo = input('Ingresa tu nombre: ')
age = int(input('Ingresa tu edad: '))
height = float(input('Ingresa tu estatura: '))
# utilizo un operador relacional
status = input('Eres estudiante (yes/no): ') == 'yes'

print(nombre_completo)
print(age)
print(height)
print(status)

print(type(nombre_completo))
print(type(age))
print(type(height))
print(type(status))

print(
    str("10")
)

# Multiples variables en una sola linea de codigo
nombre_completo, age, height, status = (
    "Eduardo",
    10,
    1.75,
    True
)
print(nombre_completo, age, height, status)
