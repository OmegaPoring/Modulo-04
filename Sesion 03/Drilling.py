class Banco:                                                        #Datos de banco, no los vamos a usar pero lo pedian#
    def __init__(self, nombre, codigo_de_banco, direccion):
        self.nombre = nombre
        self.codigo_de_banco = codigo_de_banco
        self.direccion = direccion

class Cliente:                                                      #Datos de cliente, necesario para las cuentas de ahorro y corriente#
    def __init__(self, nombre, direccion, numero_de_identificacion):
        self.nombre=nombre
        self.direccion=direccion
        self.numero_de_identificacion=numero_de_identificacion

    def get_nombre(self):
        return self.nombre

class Cuenta:                                                       #Clase Cuenta, almacena el Saldo (lo que mas vamos a usar) y metodos deposito y consulta#
    def __init__(self, numero_de_cuenta, titular, saldo=0):
        self.numero_de_cuenta=numero_de_cuenta
        self.titular=titular
        self.saldo=saldo

    def deposito(self, monto):
        self.saldo += monto
        print(f"Se han depositado {monto} pesos exitosamente")

    def consulta(self):
        if self.saldo < 0:                                          #Agregué esto porque me arrojaba saldo negativo (en el caso de la cuenta corriente)#
            print(f"Actualmente tienes 0 pesos en tu cuenta")       #ya le cobrarán la deuda del credito a fin de mes#
        else:
            print(f"Actualmente tienes {self.saldo} pesos en tu cuenta")

class Ahorro(Cuenta):                                               #Clase para cuenta de ahorro, contiene atributo "cantidad de retiro" (ademas de los de clase padre)#
    def __init__(self, numero_de_cuenta, titular, saldo=0, cantidad_de_retiros=0):
        super().__init__(numero_de_cuenta, titular, saldo)
        self.cantidad_de_retiros=cantidad_de_retiros

    def retiro(self, monto):                                        #Tambien tiene metodos de retiro, transferencia y get cantidad de retiros#
        if self.saldo >= monto:                                     #(para que imprima la cantidad de retiros que se han hecho)#
            self.saldo -= monto
            self.cantidad_de_retiros += 1
            print(f"Se han retirado {monto} pesos exitosamente, tu nuevo saldo es {self.saldo} pesos")
        else:
            print("no tienes saldo suficiente para realizar tu retiro")

    def transferencia(self, monto, cuenta):
        if self.saldo >= monto:
            self.saldo -= monto
            self.cantidad_de_retiros += 1
            cuenta.deposito(monto)
            print(f"Se ha transferido {monto} pesos exitosamente a tu cuenta corriente, tu nuevo saldo es {self.saldo} pesos")
        else:
            print("no tienes saldo suficiente para realizar tu retiro")
        
    def get_cantidad_de_retiros(self):
        if self.cantidad_de_retiros == 1:
            print(f"Has realizado solo {self.cantidad_de_retiros} retiro")
        else:    
            print(f"Has realizado un total de {self.cantidad_de_retiros} retiros")

class Corriente(Cuenta):                                            #Lo mismo que la cuenta Ahorro, solo que en lugar de "cantidad de retiro" tiene "limite de retiro"#
    def __init__(self, numero_de_cuenta, titular, saldo=0, limite_de_retiro=0):
        super().__init__(numero_de_cuenta, titular, saldo)
        self.limite_de_retiro=limite_de_retiro

    def retiro(self, monto):                                        #if y elifs por si excede su monto pero aun le queda credito y demases#
        if self.limite_de_retiro >= monto and self.saldo >= monto:
            self.saldo -= monto
            print(f"Se han retirado {monto} pesos exitosamente, tu nuevo saldo es {self.saldo} pesos")
        elif (self.limite_de_retiro + self.saldo) >= monto:
            self.saldo -= monto
            self.limite_de_retiro += self.saldo
            print(f"Has excedido la cantidad de dinero que tienes en tu cuenta, se ha restado saldo de tu linea de credito, el monto restante de tu credito es {self.limite_de_retiro} pesos")
        else:
            print(f"Excedes tu limite de retiro, recuerda que tu limite de retiro es de {self.limite_de_retiro} pesos")

    def transferencia(self, monto, cuenta):
        if self.limite_de_retiro >= monto and self.saldo >= monto:
            self.saldo -= monto
            cuenta.deposito(monto)
            print(f"Se ha transferido {monto} pesos exitosamente a tu cuenta de ahorro, tu nuevo saldo es {self.saldo} pesos")
        elif (self.limite_de_retiro + self.saldo) >= monto:
            self.saldo -= monto
            self.limite_de_retiro += self.saldo
            cuenta.deposito(monto) #<------no pense que esto funcionaria#
            print(f"Has excedido la cantidad de dinero que tienes en tu cuenta, se ha restado saldo de tu linea de credito, el monto restante de tu credito es {self.limite_de_retiro} pesos")
        else:
            print(f"Excedes tu limite de retiro, recuerda que tu limite de retiro es de {self.limite_de_retiro} pesos")


cliente1=Cliente("Pedrito Ramirez", "Calle 1", "999999999") #Nombre, drieccion, numero de identificacion#
ahorro1=Ahorro("001", cliente1.get_nombre())                #Numero de cuenta, titular (extraido de los datos del cliente)#
corriente1=Corriente("002", cliente1.get_nombre(), 0, 50000) #numero de cuenta, titular, saldo inicial, limite de retiro#

ahorro1.deposito(5000)
ahorro1.consulta()
ahorro1.retiro(6000)
ahorro1.retiro(3000)
ahorro1.get_cantidad_de_retiros()
ahorro1.retiro(1000)
ahorro1.get_cantidad_de_retiros()
ahorro1.deposito(10000)
ahorro1.transferencia(5000, corriente1)
corriente1.consulta()
ahorro1.consulta()
corriente1.retiro(6000)
corriente1.deposito(2000)
corriente1.consulta()
corriente1.transferencia(50000, ahorro1)
ahorro1.consulta()
corriente1.consulta()
corriente1.retiro(1000)