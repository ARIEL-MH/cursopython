# una tupla es un estructura de datos
# permite manejar diferentes tipos de datos
# son inmutables
# son objetos inmutables
# esta se quedara asi por el resto del programa

# tambien se rigen por los indices positivos y negativos
settings = (
    "localhost",  # 0
    3306,  # 1
    True  # 2
)

print('----------')
print(settings[0])
print(settings[1])
print(settings[2])

print('----------')
print(settings[-1])

print(settings)
print(type(settings))


# print(settings[10])  # Da error
# son utilizados para valores que se conocen de antemano y no cambian
# se usan para fines de lectura

# Podemos crear tuplas sin el uso de parentesis
# numbers = 1, 2, 3, 4, 5
numbers = 1,  # python reconoce que es una tupla de un solo elemento
print(numbers)
print(type(numbers))

# DESEMPAQUETADO DE TUPLAS
courses = (
    "Python",  # 0
    "Django",  # 1
    "Ruby",  # 2
    "Ruby on Rails",  # 3
    "Mysql",  # 4
    "MongoDB"
)

print(courses[0])

# Generar diferentes variables para asignar los valores de mi tupla
# var1, var2, var3, var4, var5 = courses[0], courses[1], courses[2], courses[3], courses[4]
# var1, var2, var3, var4, var5 = courses

# var1 = courses[0]
# var2 = courses[1]
# var3 = courses[2]
# var4 = courses[3]
# var5 = courses[4]

# print(var1, var2, var3, var4, var5)

# Podemos omitir ciertos valores y agruparlos

# _ vamos a denotar que vamos a pasar de los valores de la tupla o omitir
# var1, _, var3, var4, var5, _ = courses

# print(var1, var3, var4, var5)
# print(_)

print(courses)
# var1, var2, *sub_courses, _, last_value = courses
var1, var2, *_, last_value = courses
print(
    var1,
    var2,
    # sub_courses,
    last_value
)

# ZIP la funcion zip no permite trabajar con diferentes colecciones
# y apartir de ellas generemos tuplas

users = ["user1", "user2", "user3"]
courses = ("Python", "Django", "Rails")
scores = [10, 8, 7]
# unimos las coleciones usando sus indices
response = list(zip(users, courses, scores))
response = tuple(zip(users, courses, scores))

print(response)
print(type(response))

# unir defirentes valores de diferentes colecciones
