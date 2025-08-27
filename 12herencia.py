class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False


class Admin(User):
    def __init__(self, username, password, email):
        super().__init__(username, password)
        self.email = email

    def send_email(self):
        print(f'Sending email to {self.email}')

    def login(self, username, password):
        # if self.username == username and self.password == password:
        #     self.send_email()
        #     return True
        # return False
        if super().login(username, password):  # SUPER LLAMA a la clase padre podemos reducir lienas de codigo
            self.send_email()
            return True
        return False


class Organizer(User):
    ...


admin = Admin('Admin1', 'adminpassword', 'admin1@example.com')
organizer = Organizer(
    'Organizer1', 'organizerpassword')

print(organizer.username)


print(admin.login('Admin1', 'adminpassword'))
