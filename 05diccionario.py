# los diccionarios son estructuras de datos que almacenan pares de clave (llave)-valor
# se definen utilizando llaves {}
# cada par de clave-valor se separa por comas
# las claves deben ser únicas e inmutables (números, cadenas, tuplas)
# los valores pueden ser de cualquier tipo (números, listas, otros diccionarios)

# estos son objectos inmutables String, tuplas, int, float boolenas
user = {
    'name': 'Cody',
    'age': 30,
    'active': True,
    'courses': [
        'Python', 'Django', 'Redis'
    ],
    'settings': (123, True),
    # 'name': 'User2',
    # 'name': 'User3',  # Toma el ultimo valor de la llave duplicada las llaves son valores unicos,
    # 10: 'Eduardo',
    # 3.14: 'Ismael',
    # True: False,
    # (1, 2, 3): 'Tupla'

}

print(user)
# ** Obtener valores

print('name' in user)

user_name = user['name']
user_name = user.get('name', 'El valor no existe.')  # user['password']
# none ausencia de un valor
print(
    user_name
)

# Edita el valor
user['name'] = 'código'
# Crea un nuevo valor
user['last_name'] = 'facilito'

print(user)

# ** Metodos key, values, items

print(
    tuple(user.keys())
)

print(
    list(user.values())
)

print(
    list(user.items())
)


# ** ACTUALIZAR DICCIONARIOS

# user['name'] = 'Código'
# user['last_name'] = 'Facilito'


# añadir una nueva llave primero ententa obtener el valor y si no exite se crea con su valor por default
id = user.setdefault('id', 100)

courses = user.get('courses', [])
courses.append('Flask')
courses.append('FastAPI')

user.update({
    'name': 'Código',
    'settings': None,
    'last_name': 'Facilito',
    'courses': courses
})

# Eliminar
# del user['active']
value = user.pop('settings')

# Borrar todas las llaves
user.clear()

print(value)
print(id)
print(len(user))
print(user)
