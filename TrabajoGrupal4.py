import random
import time

# DESARROLLO

# Hoy simularemos que nuestra tienda virtual tiene muchos usuarios comprando desesperadamente. De igual forma, 
# simularemos un alto movimiento de proveedores que renuevan nuestro stock de productos a ofrecer.

# Primero, desarrollaremos una forma de almacenar nuestro stock de dos productos. El primer producto tendrá 
# 120 unidades y el segundo 150.

stock_prodcuto1 = 120
stock_producto2= 150

# Luego, simularemos cada 3 segundos una compra de “n” unidades de cualquiera de los dos productos. 
# n representa un número aleatorio entre 1 y 10.
# Cada compra, como es natural, afecta el stock inicial de productos. Es decir, si una compra simulada es de 3 
# unidades del producto 1, este se debe descontar del stock.

compra = 0
reposicion = 0

while compra <=25 and reposicion <=2:

    if stock_prodcuto1 < 100:
            stock_prodcuto1 += 50
            print('Sumamos 50 a producto 1','stock resultante',stock_prodcuto1)
            reposicion = reposicion + 1
            print('reposicion', reposicion )

    if  stock_producto2 < 100:
            stock_producto2 += 50
            print('Sumamos 50 a producto 2','stock resultante', stock_producto2)
            reposicion = reposicion + 1
            print('reposicion', reposicion )
    

    time.sleep(3)
    n1 = random.randrange(1, 11)
    n2 = random.randrange(1, 11)
    stock_prodcuto1 -= n1
    stock_producto2 -= n2
    
    compra += 1
    print('Stock producto 1: ',stock_prodcuto1)
    print('Stock producto 2: ', stock_producto2)
    print('-------------------------------------')

    
    if compra == 11:
        compra = 0
        print('10 compras realizadas. Stock producto 1: ',stock_prodcuto1) 
        print('10 compras realizadas. Stock producto 2: ',stock_producto2) 


# Cada 10 compras, el programa debe imprimir en pantalla el número de unidades disponibles por producto. ¿Lo lograron?

# Por último, cuando un producto tenga un stock de menos de 100 unidades, los proveedores enviarán automáticamente 50 
# unidades más. Esto se debe reflejar en el stock de cada producto.

# Lamentablemente, los proveedores solo tienen stock suficiente para enviar 150 unidades en total de productos 1 y 2.
