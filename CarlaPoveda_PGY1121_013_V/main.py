from funciones import *
import time

registros = []

usuario = input("ingrese su nombre y apellido\n")
sw = True
while sw:  

    print("****Registro de vehiculos de automotora AutoSeguro***")
    print("")
    print("")
    print("***Menú***")
    print("1.Grabar registro de vehiculo.")
    print("2.Buscar registro de vehiculo.")
    print("3.Imprimir certificados")
    print("4.Salir")
    
    op = int(input("Ingrese la opción que desea usar\n"))
    if op > 0 and op <= 4:
        if op == 1:
            grabar()
        elif op == 2:
            buscar()
        elif op == 3:
            imprimir()
        elif op == 4:
            print(f"Hasta pronto {usuario}.\nVer. 1.0")
            time.sleep(5)
            sw = False
    else:
        print("Dato inválido, vuelva a ingresar")
        time.sleep(5)
    
    