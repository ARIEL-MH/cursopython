class ClaseZ:
    def say_hello(self):
        print("Hello from ClaseZ")


class ClaseA(ClaseZ):
    # def say_hello(self):
    #     print("Hello from ClaseA")
    ...


class ClaseB:

    def say_hello(self):
        print("Hello from ClaseB")

    def say_goodbye(self):
        print("Goodbye from ClaseB")


class ClaseC(ClaseA, ClaseB):
    ...

# Recomendacion evitar la herencia multiple
# Evitar que las clases sobrescriban los métodos


c = ClaseC()
c.say_hello()  # Llama a ClaseA.say_hello() por el orden de herencia busca de izquierda a derecha
c.say_goodbye()
