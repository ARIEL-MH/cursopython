"""
class <NombreClase>(): # aqui puden ser opcionales los parentesis
    ...

mi_variable = <NombreClase>()
"""


class User:
    username = ''
    password = ''
    email = ''


# Podemos instaciar n objectos
user1 = User()
user2 = User()

# Modificamos
user1.username = 'Juan'
user1.password = '1234'
user1.email = 'juan@example.com'

user2.username = 'Pablo'
user2.password = '13243'
user2.email = 'pablo@example.com'

# Consultamos
# print(user1.username)
# print(user1.password)
# print(user1.email)
# print('--------------')
# print(user2.username)
# print(user2.password)
# print(user2.email)

# print(user1)
# print(type(user1))


# Clase


class Usuario:

    # Esto es un parametro por lo cual deben tener un parametro que haga referencia al objecto perse
    # por convención utilizar self
    # ** Metodo init
    def __init__(self, username, password, email=None):
        self.username = username
        self._password = password  # Privado pero si se puede editar y acceder "privado"
        # __ (Name Mangling) ofuscar acceder o modifcar atriburos privados
        self.email = email

    # Metodos
    def mostrar_info(self):  # El metodo tambien recibe self
        print(f"Usuario: {self.username}", f"Email: {self.email}")

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login exitoso")
            self.mostrar_info()  # Podemos llamar a otros metodos
        else:
            print("Login fallido")


usuario1 = Usuario('Juan', '1234')
usuario2 = Usuario(
    username='Pablo',
    password='13243',
    email='pablo@example.com'
)

# Evitar añadir atributos fuera del metodo init
usuario1.isAdmin = True  # Dinámicamente añade un nuevo atributo
usuario1.courses = [
    "Python",
    "Django",
    "Flask"
]

usuario1.__dict__['active'] = False

# print(usuario1.username)
# print(usuario1.password)
# print(usuario1.email)
# print(usuario1.isAdmin)
# print(usuario1.courses)
# print(usuario1.__dict__)  # Muestra los atributos del objeto
# print('--------------')
# print(usuario2.username)
# print(usuario2.password)
# print(usuario2.email)

# Asi se llama al método
usuario1.mostrar_info()
usuario1.login('Juan', '1234')

print('--------------')
