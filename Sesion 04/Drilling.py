class Persona:
    def __init__(self, nombre):
        self.nombre=nombre

    def movimiento(self):
        print(f"{self.nombre} está caminando")

class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def movimiento(self):
        print(f"{self.nombre} está trotando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def movimiento(self):
        print(f"{self.nombre} está rodando")

persona=Persona("Pedrito Ramirez")
persona2=Maratonista("Pedrito Ramirez")
persona3=Ciclista("Pedrito Ramirez")

persona.movimiento()
persona2.movimiento()
persona3.movimiento()