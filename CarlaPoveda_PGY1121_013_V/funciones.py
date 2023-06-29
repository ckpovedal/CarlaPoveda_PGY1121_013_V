registros = []

#Validación de patente
def validar_patente(patente):
    if len(patente) >= 6:
        return True
    if not patente[6:].isadigit():
        return False
    if not patente[6:].isalpha():
        return False
    return

#validación de precio
def validar_precio(precio):
    if precio < 5000000:
        return False

#Validación de marca
def validar_marca(marca):
    if len(marca) < 2 and len(marca) > 15:
        return False  


def grabar():
    patente = input("Ingrese el número de patente: \n")
    if not validar_patente(patente):
        print("El registro de patente es invalido, vuelva a ingresar")
        return
    
    nombreD = input("Ingrese el nombre completo del propietario: \n")
    if len(nombreD) < 8:
        print("El nombre debe tener 8 caracteres o más.")
        return
    
    tipoV = input("Ingrese el tipo de vehiculo: \n")
    
    marca = input("Ingrese la marca del vehiculo: \n")
    if validar_marca(marca):
        print("Ingrese una marca que contenga entre 2 a 15 caracteres")
        return
    
    
    precio = int(input("Ingrese el valor del vehiculo: \n"))
    if validar_precio(precio):
        print("Debe ingresar un monto mayor a 5 millones")
        return
    
    multa = input("Si registra multas ingrese fecha (DD-MM-YYYY) y valor, si no N/A\n")
        
    fecha_registro = input("Ingrese la fecha de registro de Vehiculo (DD-MM-YYYY)\n")

    registros.append([patente, nombreD, tipoV, marca, precio, multa, fecha_registro])
    
    print("Datos grabados correctamente.")
