# SPRINT DE ENTREGA:
# Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante el Módulo 1: Python básico. Por tanto, se debe poner foco en lo siguiente:
# Comentar debidamente el código para que sea comprensible por un tercero.
# El programa tiene tres partes: manejo de bodega, información clientes y sistema de envío.
# Cada parte debe entregarse en un script diferente.

# Información clientes
# ● Debe crear una base de datos que tenga información de clientes: ID, nombre, apellido, edad y contraseña.
# Cree 4 clientes iniciales para probar el programa.
# ● Diseñe tres funciones:
# - la primera debe agregar nuevos clientes,
# - la segunda debe eliminar clientes según ID.
# - la tercera debe mostrar toda la información por cliente.

# Creamos la función clientes(registro_clientes:int) para ingresar los clientes.

def clientes(registro_clientes:int):
    clientes = {}
    for cliente in range(registro_clientes): #En el ciclo for creamos un range para limitar el ingreso porterriormente de clientes en 4.
        rut = input("Rut cliente: ") # Se solicitan los datos de ingreso de los clientes solicitados en el ejercicio.
        nombre = input("Nombre cliente: ")
        apellido = input("Apellido cliente: ")
        edad = input("Edad cliente: ")
        password = input("Contraseña cliente: ")
        clientes[rut] = [nombre, apellido, edad, password] # Agregamos los datos a un diccionario con clave rut. 
    return clientes # Realizamos un return para obtener el diccionario resultante.

lista_clientes = clientes(4) # Llamamos a la función para que se ejecute y la almacenamos en una variable llamada lista_clientes
print(lista_clientes) # Mostramos la lista clientes
print("-------------------------------------------------------------------------------------------------------------------------------------")

# Creamos la función nuevo_cliente(diccionario) para ingresar nuevos clientes.

def nuevo_cliente(diccionario):
    clientes_nuevos = int(input("¿Cuántos clientes desea ingresar?: "))         # Se ingresa el número de clientes que se quiere ingresar
    for cliente in range(clientes_nuevos):          # El ciclo for está limitado por el input de número de clientes.
        rut = input("Rut cliente: ")          # Se solicitan los datos de ingreso de los clientes solicitados en el ejercicio.
        nombre = input("Nombre cliente: ")
        apellido = input("Apellido cliente: ")
        edad = input("Edad cliente: ")
        password = input("Contraseña cliente: ")
        diccionario[rut] = [nombre, apellido, edad, password]       # Agregamos los datos a un diccionario con clave rut. 
    print(f'Se actualizaron {clientes_nuevos} clientes')        # Indicamos el número de clientes nuevos.
    print(lista_clientes)

nuevo_cliente(lista_clientes)         # Llamamos a la función para que se ejecute y agregue a los nuevos clientes.
print("-------------------------------------------------------------------------------------------------------------------------------------")

# Para eliminar un cliente por su rut, creamos la siguiente función:

def eliminar_cliente(diccionario):
    eliminar = input("Ingrese el rut del cliente que desea eliminar: ")      # Se solicita el rut del cliente a eliminar.
    del diccionario[eliminar]       # Con la función del eliminamos el ítem. 
   
eliminar_cliente(lista_clientes)        # Llamamos a la función para que se ejecute y elimine a un cliente.
print(lista_clientes)                   # Mostramos como se encuentra el diccionario lista_clientes
print("-------------------------------------------------------------------------------------------------------------------------------------")

# Para mostrar los clientes ingresados, creamos la siguiente función: 

def informacion_clientes(diccionario:dict):
    print("Lista clientes ingresados")
    for clave, valor in diccionario.items():        # Ciclo for recorre los items del diccionario.
        print(clave, ":", valor)                    # Mostramos los clientes, clave y valor del diccionario

informacion_clientes(lista_clientes)         # Llamamos a la función para que se ejecute y mostramos a los clientes.