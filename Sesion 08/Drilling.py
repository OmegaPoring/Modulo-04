try:    
    informacion = open("informacion.dat", "x")
    i=1
    while i<=5:
        informacion.write(f"Datos de informacion  en la linea {i}\n")
        i=i+1
    informacion.close()    
except:
    informacion = open("informacion.dat", "w")
    informacion.write("El archivo informacion.dat ya existe, ha sido creado previamente\n")
    i=1
    while i<=5:
        informacion.write(f"Datos de informacion  en la linea {i}\n")
        i=i+1
    informacion.close()

def lector():
    informacion = open("informacion.dat", "r")
    contenido=informacion.readlines()
    for frase in contenido:
        print(frase)
    informacion.close()
    
lector()