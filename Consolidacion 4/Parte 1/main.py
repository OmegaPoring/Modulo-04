class Vehiculo:
    def __init__(self, marca, modelo, numero_de_ruedas):
        self.marca=marca
        self.modelo=modelo
        self.numero_de_ruedas=numero_de_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc"
        
cantidad=int(input("Cuantos vehiculos desea insertar: "))
conjunto=[]
i=1
while i <= cantidad:
    print(f"\nDatos del automóvil {i}")
    marca=input("Inserte la marca del automóvil: ")
    modelo=input("Inserte el modelo: ")
    ruedas=int(input("Inserte el número de ruedas: "))
    velocidad=int(input("Inserte la velocidad en km/h: "))
    cilindraje=int(input("Inserte el cilindraje en cc: "))
    auto=Automovil(marca, modelo, ruedas, velocidad, cilindraje)
    conjunto.append(auto)
    i+=1

print("\nImprimiendo por pantalla los Vehiculos: \n")
i=1
while i <= cantidad:
    print(f"Datos del automóvil {i} : {conjunto[i-1].imprimir()}")
    i+=1