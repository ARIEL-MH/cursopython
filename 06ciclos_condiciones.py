# ** None
# .get('lave') -> None

# Rrepresenta la ausencia de un valor

from random import randint
user = None  # user no alamacena absolutamente nada
# se puede representar Null o Nil

print(user)


# ** True / False
# '', 0, 0.0, False, [], (), {}, None. Todos estos valores son falso
# Todo lo que no sea lo anterior es positivo
# " ", 'a', 1, -1, 1.0, -1, [1], (1), []


# ** Condiciones

# Estructura
"""
if <bool (True)>:
    Aqui va la lógica
    y tiene que ir identado 
    port 4 espacios
"""

number = 10
number2 = 20

result = number > number2  # False

if result:
    print(f"{number} es mayor que {number2}")
else:
    print(f"{number} no es mayor que {number2}")


# esto hace un código pythonico
value = 'Cody'

if value:
    print('>>> Pose un valor')
else:
    print(">>> Este bloque se ejecuta cuando la condición no se cumple")

# if (len(value) > 0):
#     print('>>> Pose un valor')


# ** Condiciones anidadas

# evitar en la mayoria de veces evitar las condiciones anidadas
if number >= 10:
    print(f"{number} es mayor o igual que 10")

    if number > number2:
        print(f"{number} es mayor que {number2}")
    else:
        print(f"{number} no es mayor que {number2}")


# ** ELIF

# Evaluar diferente condiciones

color = 'Rojo'

# if color == 'Verde':
#     print('Puedes continuar')
# else:
#     if color == 'Amarillo':
#         print('Precaución')
#     if color == 'Rojo':
#         print('Detente')

# Asi mejoramos el codigo anterior
if color == 'Verde':
    print('>>> Puedes continuar...')
elif color == 'Amarillo':
    print('>>> Precaución.')
elif color == 'Rojo':
    print('>>> Detente.')
else:
    print('>>> Color no identificado.')

# ** MATH
# Evaluar diferentes casos
score = 10

match score:
    case 10:
        print('>>> Muchas felicidades, tu calificacion es 10')
    case 9 | 8:  # se utiliza or con el |
        print('>>> Felicidades, tu califición es aprobatoria!')
    case 6 | 7:
        print('>>> Aprobaste la materia!')
    case _:  # igual al default
        print('>>> Lo sentimos, calificación NO aprobatoria.')

# Ahora con el if

if score == 10:
    print('>>> Muchas felicidades, tu calificacion es 10')
elif score == 9 or score == 8:
    print('>>> Felicidades, tu califición es aprobatoria!')
elif score == 6 or score == 7:
    print('>>> Aprobaste la materia!')
else:
    print('>>> Lo sentimos, calificación NO aprobatoria.')

# ** Operador Ternario
age = 19

# Condicionar utilizando una sola linea de código
# One liner
message = 'Eres mayor de edad' if age >= 18 else 'Eres menor de edad'
print(message)


# ** for-each & while


numbers = [1, 2, 3, 4, 5]
tuplas = (20, 5, 6, 15)
message = 'Hola Mundo'

user = {
    'nombre': 'Cody',
    'edad': 30,
    'contrasenia': '12345'
}

"""
for <variable> in <iterable>:
    <bloque de código>
"""

# for number in numbers:
#     print(f'{number}')

# for caracter in message:
#     print(caracter)

print(user.items())
# Desempaquetado de tuplas
for key, value in user.items():
    print(f"{key}: {value}")

# ** range
# Rango de numero enteros que es un colección
# range(10) # 0 - 9
# range (start, stop + 1)

# for number in range(5, 10 + 1):
#     print(f'{number}')

courses = ['Python', 'Go', 'Rust', 'Django', 'Java']
# for index in range(len(courses)):
#     print(f'Index: {index}, Value: {courses[index]}')
# recomendación range para trabajar con rangos con número enteros

for course in courses:
    print(course)

# ** while

"""
while <condition>
    <bloque de código>
"""

counter = 0

# usar si no sabemos cuantas iteraciones vamor a utilizar

# while counter < 10:
#     print(f'Valor: {counter}')
#     # counter = counter + 1
#     counter += 1  # esta opción es más pythonica


for number in range(10):
    print(f'Valor: {number}')

number = input('Ingresa un número: ')
number = int(number)  # convertir a entero

counter = 0
# Contar el número de dígitos de un número
while number > 0:
    number = number // 10
    counter += 1
else:
    print('La cantidad de dígitos es:', counter)

# Juego del número mágico, random

number = None
random_number = randint(0, 20)
hits = 0

while number != random_number and hits <= 5:
    number = input('Adivina el número (0-20): ')
    number = int(number)  # convertir a entero

    if random_number > number:
        print('El número es mayor')
    else:
        print('El número es menor')

    hits += 1
else:
    if number != random_number:
        print(f'Lo siento, has perdido. El número era: {random_number}')
    else:
        print(f'Felicidades, encontrastes el número. {random_number}')

# ** Break && Continue
