class Persona():
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_edad(self, edad):
        self.edad = edad

    def set_estatura(self, estatura):
        self.estatura = estatura

    def set_peso(self, peso):
        self.peso = peso

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_sexo(self):
        return self.sexo

    def get_edad(self):
        return self.edad

    def get_estatura(self):
        return self.estatura

    def get_peso(self):
        return self.peso
    
    def get_full_info(self):
        return f"{self.nombre} {self.apellido}, {self.sexo}, {self.edad}, {self.estatura}, {self.peso}"
    
Persona_1=Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 mts", "68 Kg.")
Persona_2=Persona("Juan", "Camargo", "Masculino", "18 años", "1.80 mts", "75 Kg.")

print(Persona_1.get_full_info())
print(Persona_2.get_full_info())
print("---------------------------------------------")

Persona_1.set_edad("21 años")
Persona_2.set_apellido("Santiago")

print(Persona_1.get_full_info())
print(Persona_2.get_full_info())