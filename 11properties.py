# Son forma elegante de como obtener y actualisar valores de nuestro atributo

class User:
    def __init__(self, username, password, email=None, rol='Organizer'):
        self.username = username
        self._password = password  # Valor privado
        self.email = email
        self.rol = rol

    # Getter y Setter
    @property
    def password(self):
        if self.rol == 'Admin':
            return self._password
        else:
            return None

    @password.setter
    def password(self, new_password):
        if self.rol != 'Admin':
            return
        self._password = new_password


user1 = User("alice", "securepassword", rol='Admin')

user1.password = "newsecurepassword"
print(user1.password)  # Output: newsecurepassword
