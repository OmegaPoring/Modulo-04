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

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada, peso_de_carga):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self.peso_de_carga=peso_de_carga

    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc, Carga: {self.peso_de_carga} Kg"
    
class Particular(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada, numero_de_puestos):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
        self.numero_de_puestos=numero_de_puestos

    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas {self.velocidad} Km/h, {self.cilindrada} cc, Puestos: {self.numero_de_puestos}"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo_de_bicicleta):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo_de_bicicleta=tipo_de_bicicleta
        
    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas, Tipo: {self.tipo_de_bicicleta}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo_de_bicicleta, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_de_ruedas, tipo_de_bicicleta)
        self.nro_radios=nro_radios
        self.cuadro=cuadro
        self.motor=motor
        
    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas, Tipo: {self.tipo_de_bicicleta}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

cantidad=int(input("Cuantos vehiculos desea insertar: "))
conjunto=[]
i=1
while i <= cantidad:
    tipo=int(input(f"Ingrese el tipo del vehiculo numero {i}:\n1.-Automóvil de Carga\n2.-Automóvil Particular\n3.-Bicicleta\n4.-Motocicleta\n"))
    if tipo == 1:
        print(f"\nDatos del vehiculo {i}")
        marca=input("Inserte la marca del automóvil: ")
        modelo=input("Inserte el modelo: ")
        ruedas=int(input("Inserte el número de ruedas: "))
        velocidad=int(input("Inserte la velocidad en km/h: "))
        cilindraje=int(input("Inserte el cilindraje en cc: "))
        peso_de_carga=int(input("Inserte el peso maximo de carga: "))
        auto=Carga(marca, modelo, ruedas, velocidad, cilindraje, peso_de_carga)
        conjunto.append(auto)
        i+=1
    elif tipo == 2:
        print(f"\nDatos del vehiculo {i}")
        marca=input("Inserte la marca del automóvil: ")
        modelo=input("Inserte el modelo: ")
        ruedas=int(input("Inserte el número de ruedas: "))
        velocidad=int(input("Inserte la velocidad en km/h: "))
        cilindraje=int(input("Inserte el cilindraje en cc: "))
        numero_de_puestos=int(input("Inserte la cantidad maximo de puestos: "))
        auto=Particular(marca, modelo, ruedas, velocidad, cilindraje, numero_de_puestos)
        conjunto.append(auto)
        i+=1
    elif tipo == 3:
        print(f"\nDatos del vehiculo {i}")
        marca=input("Inserte la marca de la bicicleta: ")
        modelo=input("Inserte el modelo: ")
        ruedas=int(input("Inserte el número de ruedas: "))
        tipo_de_bicicleta=input("inserte el tipo de bicicleta (urbana o carrera): ")
        auto=Bicicleta(marca, modelo, ruedas, tipo_de_bicicleta)
        conjunto.append(auto)
        i+=1
    elif tipo == 4:    
        print(f"\nDatos del vehiculo {i}")
        marca=input("Inserte la marca de la motocicleta: ")
        modelo=input("Inserte el modelo: ")
        ruedas=int(input("Inserte el número de ruedas: "))
        tipo_de_bicicleta=input("inserte el tipo de motocicleta: ")
        radio=int(input("Ingrese el numero de radios: "))
        cuadro=input("Ingrese el tipo de cuadro: ")
        motor=input("Ingrese el tipo de motor: ")
        auto=Motocicleta(marca, modelo, ruedas, tipo_de_bicicleta, radio, cuadro, motor)
        conjunto.append(auto)
        i+=1

print("\nImprimiendo por pantalla los Vehiculos: \n")
i=1
while i <= cantidad:
    print(f"Datos del automóvil {i} : {conjunto[i-1].imprimir()}")
    i+=1

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print(f"\nMotocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")