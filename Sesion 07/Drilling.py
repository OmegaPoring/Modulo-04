class RangoSalarioError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def verification(value):
        if value <= 2000 and value >=1000:
            print("El valor ingresado es correcto")
        else:
            raise RangoSalarioError(message)
        
value=int(input("Ingrese el salario: "))

message=f"{value} -> Salario no está definido en el rango (1000 a 2000)"

RangoSalarioError.verification(value)