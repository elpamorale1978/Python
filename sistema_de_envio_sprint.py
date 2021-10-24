# SPRINT DE ENTREGA:
# Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante el Módulo 1: Python básico. Por tanto, se debe poner foco en lo siguiente:
# Comentar debidamente el código para que sea comprensible por un tercero.
# El programa tiene tres partes: manejo de bodega, información clientes y sistema de envío.
# Cada parte debe entregarse en un script diferente.

# Sistema de envío
# ● El sistema de envío debe ser un programa que pregunta qué tipo de envío es necesario (Rápido o largo)
# ● Si es un envío a una distancia de más de 1.000 km es considerado largo. Si es igual o menor a la distancia de 
# 1.000 km es considerado rápido.
# ● En el caso que sea un envío rápido debe enviarse a una Bodega_A, caso contrario debe ser almacenado a una Bodega_B.
# ● El programa debe verificar que cada bodega no supere las 500 unidades.

# Creamos dos listas correspondientes a las bodegas a y b respectivamente, en las cuales se almacenan los kilometros de un envío. 

bodegaA = []
bodegaB = []

# La siguiente función indica si el envío será almacenado y en que bodega. 

def envio():
    km_envio = int(input("Ingrese cuántos kilómetros debe recorrer el envío: ")) # Preguntamos por la distancia de la entrega. 
    if km_envio <= 1000:      # Condición para entregas con distancias menores a 1000 km.
        print("Su envío es de tipo rápido")           # Indicamos que la entrega es de tipo rápido.
        if len(bodegaA) > 500:                        # Condición que nos permite saber el número de envíos alamcenados en la bodega.
            print("La bodega supero los 500 envíos. No será almacenado")     # Si es mayor a 500 las unidades existentes, indicamos que no se almacenará.
        else:
            bodegaA.append(km_envio) # Si no supera las 500 unidades, se almacena el producto en la bodega A; se ingresa a la lista
            print("El envío será almacenado en la Bodega A") # con la función append. 
            print(bodegaA)
    else:           # Condición para entregas con distancias mayores a 1000 km.
        print("Su envío es de tipo largo")           # Indicamos que la entrega es de tipo lento.
        if len(bodegaB) > 500:
            print("La bodega supero los 500 envíos. No será almacenado")     # Si es mayor a 500 las unidades existentes, indicamos que no se almacenará.
        else:
            bodegaB.append(km_envio)      # Si no supera las 500 unidades, se almacena el producto en la bodega A; se ingresa a la lista
            print("El envío será almacenado en la Bodega B")      # con la función append. 
            print(bodegaB)

envio() # Llamamos a la función para que se ejecute. 

        