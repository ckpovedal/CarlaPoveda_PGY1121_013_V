from funciones import *
import time

registros = []

sw = True
while sw:
    
    print("****Registro de vehiculos de automotora AutoSeguro***")
    print("")
    print("")
    print("***Menú***")
    print("1.Grabar registro de vehiculo.")
    print("2.Busar registro de vehiculo.")
    print("3.Imprimir certificados")
    print("4.Salir")
    
    op = int(input("Ingrese la opción que desea usar\n"))
    
    try:
        if op > 0 and op <= 4:
            if op == 1:
                grabar()
            elif op == 2:
                print("codigo incompleto :(")
            elif op == 3:
                print("codigo incompleto :(")
            elif op == 4:
                print("Codigo incompleto :(")
        else:
            print("Dato inválido, vuelva a ingresar")
            time.sleep(5)         
    except:
        print("Dato inválido, vuelva a ingresar")
        time.sleep(5)
    
    