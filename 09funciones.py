# ** Funciones
# Aprender las funciones seremos capaces
# de cambiar de paradigma

# Estructura de una función
# La funciones pueden retornar algun tipo de valor
# Las funciones deben de realizar una sola acción

"""
def <nombre_de_la_fun>(<parámetros, >):
    <cuerpo_de_la_funcion>
"""

# -------------Parámetros son opcionales


def count_to(number: int) -> None:
    for n in range(1, number + 1):
        print(n)


def multiply(number1, number2):
    result = number1 * number2
    return result


def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    return full_name


# count_to(10)  # Argumento
# multiply(5, 3)  # Argumentos
# full_name('Danny', 'Monge', 'Ing.')  # Argumentos

result = multiply(5, 3)
user_full_name = full_name('Danny', 'Monge', 'Ing.')

print(
    result,
    f'user_full_name: {user_full_name}'
)


def division(number1, number2):
    if number2 == 0 or number2 == 0:
        return None  # corto circuito
    return number1 / number2


print(
    division(0, 0.5)
)

# ** Retornar Multiples Valores


def func():
    return 'Cody', True, 12  # Usa una Tupla para retornar multiples valores


result = func()

username, _, edad = result  # desampequetado de tuplas

print(username, edad)


# ** Valores por Nombre y Posición

def full_name(first_name, last_name, prefix):
    full_name = f'{prefix} {first_name} {last_name}'
    return full_name


print(
    full_name('Danny', 'Monge', 'Ing.'),  # Posición
    full_name(prefix='Mr.', first_name='Cody', last_name='Facilito'),  # Nombre
    full_name('Cody', last_name='Facilito', prefix='Mr.')  # Mixta
)

# ** Valores por defecto

# Se asignan de derecha a izquierda


def calculate_total(price, tax=0.15, discount=0):
    total = (price + (price * tax)) - discount
    return total


total = calculate_total(100, 0.15, 20)
print("Total:", total)

total = calculate_total(100, 0.15)  # Si no hay descuento
print("Total:", total)

total = calculate_total(640)
print("Total:", total)

# Sobrescribir los valores por default

total = calculate_total(500, tax=0.02, discount=20)
print("Total:", total)


# ** Args
""" Asi se declaran -> * Posición
 ** Nombres """


def suma(*args):
    return sum(args)


print(suma(5, 3, 10, 20, 30, 40, 440, 1000))


# podemos recibir una cantidad indefinida de argumentos se crea una tupla
def show_info(username, email, *scores):
    print(f'Username: {username}')
    print(f'Email: {email}')
    print(f'Average: {sum(scores) / len(scores)}')


show_info(
    'cody',
    'cody@example.com',
    10, 10, 10, 10, 10, 10, 10, 9
)

# ** Kwargs


def show_data(**user):
    for key, value in user.items():
        print(f'{key}: {value}')


show_data(
    username='cody',
    email='cody@example.com',
    age=30,
    password='123',
    active=True,
    courses=['Python', 'Django', 'Flask'],
    last_login='2024',
    is_super_user=True
)

# ** Args and Kwargs


def show_informacion(*args, **kwargs):  # asi se definen por conveción

    print('>>> info')
    for item in args:
        print(item)

    print('>>> details')
    for key, value in kwargs.items():
        print(f'{key}: {value}')


show_informacion(
    'Cody',
    'Facilito',
    12,
    'cody@example.com',
    cursos=['Python', 'Flask', 'Django'],
    active=True,
    last_login='2024',
    is_super_user=True
)


def funcion_restriccion(username, last_name, *args, active=True, is_superuser=False, **kwargs):
    print(username, last_name)
    print('>>> Args')
    print(args)
    print('>>> Kwargs')
    print(kwargs)
    print(active, is_superuser)


funcion_restriccion(
    'cody',
    'facilito',
    'cody@example.com',
    'password124',
    cursos=['PHP', 'Laravel'],
    id_deleted=False
)


# * Scope (Alcanse)

# Donde una variable puede ser utilizada.
# Variables globales y locales

# global se utiliza en todo el programa
# local solo se utiliza en su contexto

username = 'Cody'  # global


def show_info():
    # global username para modificar la variable global no es recomendado
    # username = 'Código Facilito'
    print(username)  # local
    # print(id(username))  # las variables tienen un id


show_info()
print(username)  # global
# print(id(username))  # global

# ** Funciones Anidadas


def outer_function():
    message = 'Hola, nos encontramos en un función anidada.'

    def inner_function():
        # nonlocal message  # para trabajar con una variable de bloque superior
        # info = 'Info value'
        print(message)

    inner_function()


outer_function()


# ** Variables como funciones

def deposit(balance, amount=0):
    return balance + amount


def withdrawal(balance, amount=0):
    if amount > balance:
        return 'Fondos insuficientes'
    return balance - amount

# ** Callbacks


def handle_operation(callback, *args, **kwargs):  # Funcion de orden superior
    result = callback(*args, **kwargs)
    print("El resultado es: ", result)

# def default(*args, **kwargs):
#     return ('>>> Lo sentimos, opción no valida')


# Variables que alamacena las funciones no es necesario el parentesis
func1 = deposit
func2 = withdrawal

print(
    func1(100, 20),  # deposit
    func2(100, 20)  # withdrawal
)


options = {
    'a': func1,
    'b': func2
}

# option = input('Ingrese una opción (a/b): ')
# balance = int(input('Ingrese el balance inicial: '))
# amount = int(input('Ingrese el monto: '))

# function = options.get(
#     option,
#     lambda *args, **kwargs: '>>> Lo sentimos, opción no valida'
# )

# handle_operation(function, balance, amount)

# ** Funciones Lambda
# No tienen un nombre

"""
lambda <párametros> : <expresión> siempre retornan un valor
"""

# suma_lambda = lambda number1, number2: number1 + number2
# print(suma_lambda(5, 3))


# ** Retornar Funciones

def factory_operation(option):  # Función de orden superior

    def deposito(balance, amount=0):
        return balance + amount

    def retiro(balance, amount=0):
        if amount > balance:
            return 'Fondos insuficientes'
        return balance - amount

    default = lambda *args, **kwargs: '>>> Lo sentimos, opción no valida'

    if option == 'deposit':
        return deposito
    elif option == 'withdraw':
        return retiro
    else:
        return default


# cajero_opciones = input('Ingrese una opción (deposit/withdraw): ')
# funcion_retorno = factory_operation(cajero_opciones)

# print(funcion_retorno(100, 20))
# print(type(funcion_retorno))


# ** Closures
# Son funciones anidades las cuales recuerdan
# y pueden aceder a las variables creadas


def multiplicar(factor):
    def multiplicar_con_factor(numero):
        return numero * factor
    return multiplicar_con_factor


var1 = 10
func_operation = multiplicar(var1)  # factor
print(func_operation(3))  # numero


# ** Decoradores

# funcion que añada funciones a otra funcion
# Concepto Open Close

"""
A(B) -> C
A(Decorador
B(Función a decorar (Base))
C (Función decorada Base + Nuevas líneas de código)
"""

# Base


def decorator(func):  # A
    def wrapper(*args, **kwargs):  # C
        print("Antes de llamar a la función")
        result = func(*args, **kwargs)
        print("Después de llamar a la función")
        return result
    return wrapper


@decorator
def base_function():
    print("Esta es la función base.")


@decorator
def suma(num1, num2):
    return num1 + num2


print(suma(5, 3))


# ** Docstrings

# Documentar funcions utilizando comentario

def full_name(first_name, last_name):
    """Retorna el nombre completo.

    Args:
        - first_name: El primer nombre.
        - last_name: El apellido.

    Return:
        String
    """
    return f"{first_name} {last_name}"


print(
    full_name.__doc__
)


def polindromo(sentence):
    """ Permite conocer si un string es, o no, un palindromo

    Args:
        - sentence (String)
    Return:
        Boolean
    Examples:
    >>> polindromo("Ana")
    True
    >>> polindromo("Anita lava la tina")
    True
    >>> polindromo("Hola Mundo")
    False
    """
    sentence = sentence.lower().replace(" ", "")
    return sentence == sentence[::-1]


# print(polindromo("Ana"))
# print(polindromo("Anita lava la tina"))
# print(polindromo("Hola Mundo"))


def average(*args):
    """Pérmite conocer el promedio de N argumentos
    Example:
    >>> average(5,5,5,5,5)
    5.0
    >>> average(10,9,8,7)
    8.5
    """
    return sum(args) / len(args)
