import os

def borrar():
    os.system("cls")

def esperar_tecla():
    input("Presiona una tecla para volver.")

registros = []

#Validación de patente
def validar_patente(patente):
    if patente is None:
        return False
    return len(patente) == 6 and patente[:4].isalpha() and patente[-2:].isdigit()

#validación de precio
def validar_precio(precio):
    if precio is None:
        return False
    return int(precio) >= 5000000

#Validación de marca
def validar_marca(marca):
    if marca is None:
        return False
    return len(marca) >= 2 and len(marca) <= 15  


def validador(texto_input, texto_error, funcion_validadora):
    valor = None
    while not funcion_validadora(valor):
        borrar()
        valor = input(texto_input)
        valor_valido = funcion_validadora(valor)
        if not valor_valido:
            print(texto_error)
            esperar_tecla()
    return valor



def grabar():
    patente_texto_input = "Patente (6 caracteres, 4 letras y 2 numeros): "
    patente_texto_error = "La patente no es valida.\nDebe tener 6 cacrateres, 4 letras y 2 numeros."
    patente = validador(patente_texto_input, patente_texto_error, validar_patente)
        
    nombreD = input("Ingrese el nombre completo del propietario: \n")
    borrar()
    if len(nombreD) < 8:
        print("El nombre debe tener 8 caracteres o más.")
        return
    
    tipoV = input("Ingrese el tipo de vehiculo: \n")
    borrar()

    marca_texto_input = "Marca (2 a 15) caracteres: \n"
    marca_texto_error = "La marca no es valida. Debe tener entre 2 a 15 caracteres.\n"
    marca = validador(marca_texto_input, marca_texto_error, validar_marca)    
    
    precio_texto_input = "Precio (mayor a 5000000): \n"
    precio_texto_error = "El precio no es valido. Debe ser mayor a 5000000"
    precio = validador(precio_texto_input, precio_texto_error, validar_precio)

    tiene_multa = int(input("¿Tiene multas? 1: Si - 2:No\n"))
    multa_monto = 0
    multa_fecha = ""

    if (tiene_multa == 1):
        multa_monto = int(input("Ingrese monto de la multa:\n"))
        multa_fecha = input("Ingrese fecha de la multa:\n")
        
    fecha_registro = input("Ingrese la fecha de registro de Vehiculo (DD-MM-YYYY)\n")
    borrar()

    registros.append([patente, nombreD, tipoV, marca, precio, multa_monto, multa_fecha, fecha_registro])
    
    print("Datos grabados correctamente.")


def buscar():
    patente = input("Ingrese la patente que desea buscar:\n")
    encontrado = False
    for vehiculo in registros:
        if vehiculo[0] == patente:
            encontrado = True
            print("Información del Vehiculo:\n")
            print("Patente: ", vehiculo[0])
            print("Propietario: ", vehiculo[1])
            print("Tipo de Vehiculo: ", vehiculo[2])
            print("Marca: ", vehiculo[3])
            print("Precio: ", vehiculo[4])
            print("Valor de multas: ", vehiculo[5])
            print("Fecha de multa: ", vehiculo[6])
            print("Fecha de registro: ", vehiculo[7])
            break
    if not encontrado:
        print("Patente no encontrada.")


def imprimir():
    patente = input("ingrese la patente a la que desea imprimir sus certificados\n")
    encontrado = False
    for vehiculo in registros:
        if vehiculo[0] == patente: 
            print("Certificado de emision de contaminantes\n")
            print("Patente: ", vehiculo[0])
            print("Propietario: ", vehiculo[1])
            print("")
            print("Certificado de anotaciones\n")
            print("Patente: ", vehiculo[0])
            print("Propietario: ", vehiculo[1])
            print("Estado: Sin anotaciones vigentes")
            print("")
            print("Certificado de multas\n")
            print("Patente: ", vehiculo[0])
            print("Propietario: ", vehiculo[1])
            print("Valor multa: ", vehiculo[5])
            print("Fecha multa: ", vehiculo[6])
            break