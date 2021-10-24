# SPRINT DE ENTREGA:
# Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante el Módulo 1: Python básico. Por tanto, se debe poner foco en lo siguiente:
# Comentar debidamente el código para que sea comprensible por un tercero.
# El programa tiene tres partes: manejo de bodega, información clientes y sistema de envío.
# Cada parte debe entregarse en un script diferente.

# Manejo de bodega
# ● Guarde la información de los productos en una bodega virtual.
# ● Los productos son vasos, cucharas, cuchillos y tenedores. Cada producto debe tener un stock aleatorio entre 300 y 
# 500 unidades y una descripción del producto.
# ● Debe definir funciones que puedan:
# ● Sumar y disminuir el número de unidades por producto.
# ● Agregar nuevos productos.
# ● Quitar productos de la bodega virtual.
# ● Mostrar todos los productos disponibles y su stock. Debe tener un desfase de un segundo entre cada producto.
# ● Verificar si un producto tiene menos de 400 unidades y enviar una alerta.

import random
import time

#Se genera una función stock que pemite generar valores al azar de esta variable, entre 300 y 500 con la función random.randint

def stock():
    return random.randint(300,500)

#Se genera un diccionario con valores de: nombre del producto, que sería la clave y una lista que almacena los valores de stock y descripción

bodega_virtual = {"vasos":[stock(),"plásticos"],"cucharas":[stock(),"bronce"],"cuchillos":[stock(),"metálicos"],"tenedores":[stock(),"oro"]}
print(bodega_virtual) #Mostramos el inventario inicial de productos
print("-------------------------------------------------------------------------------------------------------------------------------------")

# La función def variacion_stock() permite elegir entre ingresar y retirar stock de un determinado producto de la lista. 

def variacion_stock():
    producto = input("¿Desea ingresar o retirar un producto?. Debe escribir ingreso o retiro: ")
    if producto == "ingreso":                              #Condición relacionada con elección de ingreso de stock
        print(bodega_virtual.keys())                       #Mostramos el inventario inicial de productos
        producto_ingreso=input("Ingrese el nombre del producto a actualizar: ")       #Preguntamos por el producto a modificar
        ingreso = int(input("Ingrese la cantidad a agregar: "))               # Preguntamos la cantidad a agregar de producto
        bodega_virtual[producto_ingreso][0] += ingreso                        # y sumamos
        print(f"El nuevo stock de {producto_ingreso} es de {bodega_virtual[producto_ingreso]} ")   # Mostramos el resultado
    elif producto == "retiro":                     #Condición relacionada con elección de retiro de stock
        print(bodega_virtual.keys())               #Mostramos el inventario inicial de productos
        producto_retiro=input("Ingrese el nombre del producto a actualizar: ")       #Preguntamos por el producto a modificar.
        retirar = int(input("Ingrese la cantidad a retirar: "))                      # Preguntamos la cantidad a retirar de producto y restamos. 
        bodega_virtual[producto_retiro][0] -= retirar
        print(f"El nuevo stock de {producto_retiro} es de {bodega_virtual[producto_retiro]} ")      # Mostramos el resultado
    else:
        print("Error. Debe ingresar ingreso o retiro")         #Este error se presenta si el usuario escribe otra alternativa a ingreso o retiro


variacion_stock() # Llamamos a la función, para que se ejecute sobre el diccionario de bodega_virtual
print("-------------------------------------------------------------------------------------------------------------------------------------")
#Para agregar los productos creamos la función def agregar_producto(diccionario)

def agregar_producto(diccionario):
    producto_agregar = int(input("¿Cuántos productos desea agregar?: "))       #Se genera un input con la cantidad de productos 
    for producto in range(producto_agregar):                                   #a ingresar para repetir la función con un ciclo for. 
        nombre_producto = input('Nombre del producto: ')  #Preguntamos por las variables de o los productos a ingresar. 
        stock = int(input('Stock del producto: '))
        descripcion_producto = input('Descripción del producto: ')
        diccionario[nombre_producto] = [stock, descripcion_producto]    #Agregamos los productos al diccionario. 
    print(f'Se actualizaron {producto_agregar}')                        #Mostramos la cantidad de productos adicionados.
    print(bodega_virtual)                                               # Mostramos el estado de la bodega virtual.

agregar_producto(bodega_virtual)    # Llamamos a la función, para que se ejecute sobre el diccionario de bodega_virtual
print("-------------------------------------------------------------------------------------------------------------------------------------")

#Para eliminar productos creamos la función def eliminar_producto(diccionario)

def eliminar_producto(diccionario):
    eliminar = input("Ingrese el nombre del producto que desea eliminar: ")    #Ingresamos el nombre del producto a eliminar.
    del diccionario[eliminar]                    #Con la función del eliminamos el item del diccionario. 
    
eliminar_producto(bodega_virtual) # Llamamos a la función, para que se ejecute sobre el diccionario de bodega_virtual
print(bodega_virtual)             # Mostramos el estado de la bodega virtual. 
print("-------------------------------------------------------------------------------------------------------------------------------------")
# Par mostrar los productos, creamo la función def mostrar_producto(diccionario).

def mostrar_producto(diccionario:dict):
    print("Productos disponibles")
    for clave, valor in diccionario.items():    # Con un ciclo for recorremos el diccionario.
        time.sleep(1)                           # Con la función time.sleep generamos un delay de un segundo.
        print(f"{clave} : {valor[0]}")          # Se muestran los productos con su repectivo stock.

mostrar_producto(bodega_virtual) # llamamos a la función, para que se ejecute sobre el diccionario de bodega_virtual
print("-------------------------------------------------------------------------------------------------------------------------------------")
# Para generar la alerta de un stock inferior a 400 unidades, creamos la siguiente función:  

def verificar_stock(diccionario:dict):
    for clave, valor in diccionario.items():  # Con un ciclo for recorremos el diccionario.
        if valor[0]< 400:                     # Condición que indica un stock menor a 400
            print(f"Hay menos de 400 unidades de {clave}") # Alerta

verificar_stock(bodega_virtual) # Llamamos a la función, para que se ejecute sobre el diccionario de bodega_virtual