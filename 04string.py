'''
Los strings son colecciones inmutables de caracteres.
'''
message = 'Hola mundo!'

print(message[0])
print(type(message))
print(len(message))
# message[0] = 'h'  # Error, los strings son inmutables
print('!' in message)
print(message.index('mundo'))
print(message[-1])

message2 = message[:]
message2 = 'h' + message[1:]
print(message2)

# ** MÉTODOS DE LOS STRINGS
# split -> genera una lista de strings
# join -> genera un string a partir de una lista

courses = 'Python, PHP, Ruby, Django, MongoDB, Ruby on Rails'
course_list = courses.split(', ')
print(course_list)

courses = ['Python', 'Ruby', 'Ruby on Rails', 'MongoDB']
message_courser = ' '.join(courses)
print(message_courser)
print(type(message_courser))

# ** GENERAR NUVOS STRINGS A PARTIR DE OTROS

name = 'Eduardo'
last_name = 'García'

# 1 usando el caracter + para unir dos o mas caracteres
# no se puede añadir un caracter que no sea string
full_name = name + ' ' + last_name + ' ' + str(30)
print(full_name)

# 2 usando el método join
full_name = ' '.join([name, last_name])
print(full_name)

# 3 usando (%s) se usan para trabajar con logs
full_name = 'El nombre completo es %s %s' % (name, last_name)
print(full_name)

# 4 usando el método format
# funciona de manera similar a (%s)

base = 'El nombre completo es: {} {}. Su edad es: {}.'
full_name = base.format(name, last_name, 30)
print(full_name)

# name = input('Ingrese su nombre: ')
# last_name = input('Ingrese su apellido: ')
# age = input('Ingrese su edad: ')
# active = input('¿Está activo? (Sí/No): ') == 'Sí'

# base2 = 'Información:\n Nombre: {name}\n Apellido: {last_name}\n Edad: {age}\n Active: {active}'
# full_name = base2.format(
#     name=name,
#     last_name=last_name,
#     age=age,
#     active=active
# )
# print(full_name)

# 5 usando f-strings (Python 3.6+)
# forma actual y mas recomendable
full_name = f'El nombre completo es: {"Eduardo Ismael"} {last_name}. Su edad es {10 + 20}.'
print(full_name)


# ** FUNCIÓN PRINT
nombre = 'Danny'
apellido = 'Monge'
print('Hola', nombre, apellido, sep='...')

# ** BUSQUEDA EN LISTAS
# Validar si se un caracter se encuentra en un string

title = ' Curso profesional de Python! '
title = title.strip()  # Elimina espacios al inicio y final

print(
    'curso' in title.lower(),
    title.count('o'),
    title.startswith('Curso'),
    title.endswith('!'),
    title.upper(),
)

print(
    title.find('p')
)

print('100'.isnumeric())  # va retornar verdadero si representa un entero

# convierte la primera letra en mayuscula y las demas en minusculas
message = 'código facilito'
print(message.capitalize())
print(message[0].upper() + message[1:])  # otra forma de hacerlo
