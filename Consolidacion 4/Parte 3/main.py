import csv

class Vehiculo:
    def __init__(self, marca, modelo, numero_de_ruedas):
        self.marca=marca
        self.modelo=modelo
        self.numero_de_ruedas=numero_de_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.velocidad=velocidad
        self.cilindraje=cilindraje

class Carga(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje, peso_de_carga):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindraje)
        self.peso_de_carga=peso_de_carga

    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas {self.velocidad} Km/h, {self.cilindraje} cc, Carga: {self.peso_de_carga} Kg"

    def guardar_datos_csv(self):
        archivo = open("vehiculos.csv", "a")
        datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()

    def leer_datos_csv(self):
        vehiculos = []
        archivo = open("vehiculos.csv", "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
        archivo.close()
        retorno=[]
        for i in vehiculos:
            if len(i) != 0:
                if i[0] == "<class '__main__.Carga'>":
                    retorno.append(i)
        for i in retorno:
            print(f"{i[1]}") 

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje, numero_de_puestos):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindraje)
        self.numero_de_puestos=numero_de_puestos

    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas {self.velocidad} Km/h, {self.cilindraje} cc, Puestos: {self.numero_de_puestos}"

    def guardar_datos_csv(self):
        archivo = open("vehiculos.csv", "a")
        datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()

    def leer_datos_csv(self):
        vehiculos = []
        archivo = open("vehiculos.csv", "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
        archivo.close()
        retorno=[]
        for i in vehiculos:
            if len(i) != 0:
                if i[0] == "<class '__main__.Particular'>":
                    retorno.append(i)
        for i in retorno:
            print(f"{i[1]}") 

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo_de_bicicleta):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo_de_bicicleta=tipo_de_bicicleta

    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas, Tipo: {self.tipo_de_bicicleta}"

    def guardar_datos_csv(self):
        archivo = open("vehiculos.csv", "a")
        datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()

    def leer_datos_csv(self):
        vehiculos = []
        archivo = open("vehiculos.csv", "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
        archivo.close()
        retorno=[]
        for i in vehiculos:
            if len(i) != 0:
                if i[0] == "<class '__main__.Bicicleta'>":
                    retorno.append(i)
        for i in retorno:
            print(f"{i[1]}") 

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo_de_bicicleta, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_de_ruedas, tipo_de_bicicleta)
        self.nro_radios=nro_radios
        self.cuadro=cuadro
        self.motor=motor

    def imprimir(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_de_ruedas} ruedas, Tipo: {self.tipo_de_bicicleta}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

    def guardar_datos_csv(self):
        archivo = open("vehiculos.csv", "a")
        datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()

    def leer_datos_csv(self):
        vehiculos = []
        archivo = open("vehiculos.csv", "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
        archivo.close()
        retorno=[]
        for i in vehiculos:
            if len(i) != 0:
                if i[0] == "<class '__main__.Motocicleta'>":
                    retorno.append(i)
        for i in retorno:
            print(f"{i[1]}") 

cantidad=0
while cantidad == 0:
    try:
        cantidad=int(input("Cuantos vehiculos desea insertar: "))
    except:
        print("El valor ingresado no corresponde a un numero, recuerda que debes ingresar la cantidad numerica de vehiculos.\n")
        
conjunto=[]
i=1

while i <= cantidad:
    try:
        tipo=int(input(f"Ingrese el tipo del vehiculo numero {i}:\n1.-Automóvil de Carga\n2.-Automóvil Particular\n3.-Bicicleta\n4.-Motocicleta\n"))
        if tipo == 1:
            print(f"\nDatos del vehiculo {i}")
            marca=input("Inserte la marca del automóvil: ")
            modelo=input("Inserte el modelo: ")
            ruedas=input("Inserte el número de ruedas: ")
            velocidad=input("Inserte la velocidad en km/h: ")
            cilindraje=input("Inserte el cilindraje en cc: ")
            peso_de_carga=input("Inserte el peso maximo de carga: ")
            auto=Carga(marca, modelo, ruedas, velocidad, cilindraje, peso_de_carga)
            conjunto.append(auto)
            auto.guardar_datos_csv()
            i+=1
        elif tipo == 2:
            print(f"\nDatos del vehiculo {i}")
            marca=input("Inserte la marca del automóvil: ")
            modelo=input("Inserte el modelo: ")
            ruedas=input("Inserte el número de ruedas: ")
            velocidad=input("Inserte la velocidad en km/h: ")
            cilindraje=input("Inserte el cilindraje en cc: ")
            numero_de_puestos=input("Inserte la cantidad maximo de puestos: ")
            auto=Particular(marca, modelo, ruedas, velocidad, cilindraje, numero_de_puestos)
            conjunto.append(auto)
            auto.guardar_datos_csv()
            i+=1
        elif tipo == 3:
            print(f"\nDatos del vehiculo {i}")
            marca=input("Inserte la marca de la bicicleta: ")
            modelo=input("Inserte el modelo: ")
            ruedas=input("Inserte el número de ruedas: ")
            tipo_de_bicicleta=input("inserte el tipo de bicicleta (urbana o carrera): ")
            auto=Bicicleta(marca, modelo, ruedas, tipo_de_bicicleta)
            conjunto.append(auto)
            auto.guardar_datos_csv()
            i+=1
        elif tipo == 4:
            print(f"\nDatos del vehiculo {i}")
            marca=input("Inserte la marca de la motocicleta: ")
            modelo=input("Inserte el modelo: ")
            ruedas=input("Inserte el número de ruedas: ")
            tipo_de_bicicleta=input("inserte el tipo de motocicleta: ")
            radio=input("Ingrese el numero de radios: ")
            cuadro=input("Ingrese el tipo de cuadro: ")
            motor=input("Ingrese el tipo de motor: ")
            auto=Motocicleta(marca, modelo, ruedas, tipo_de_bicicleta, radio, cuadro, motor)
            conjunto.append(auto)
            auto.guardar_datos_csv()
            i+=1
    except:
        print("\nIngrese un valor valido entre 1 a 4.\n")

print("\nImprimiendo por pantalla los Vehiculos: ")

particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print("\nLista de Vehiculos Particulares")
particular.leer_datos_csv()
print("\nLista de Vehiculos de Carga")
carga.leer_datos_csv()
print("\nLista de Vehiculos Bicicleta")
bicicleta.leer_datos_csv()
print("\nLista de Vehiculos Motocicleta")
motocicleta.leer_datos_csv()