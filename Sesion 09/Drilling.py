def reemplazo():
    informacion=open("informacion.dat", "r+")
    modificado=""
    contador=0
    for linea in informacion:
        replace=linea.replace("informacion", "procesamiento")
        modificado=modificado+replace
        lista=linea.split()
        for i in lista:
            if i == "informacion":
                contador += 1

    print(f"Se realizaron {contador} reemplazos.")
    cambiado=open("informacion.dat", "w")
    cambiado.write(modificado)
    informacion.close()
    cambiado.close()

reemplazo()