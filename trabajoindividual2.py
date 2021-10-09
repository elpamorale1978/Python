#Se crea la variable usuarios con el nombre de 7 usuarios. Variable tipo String#

import time
time.sleep(2)

usuarios = 'Jorge Manuel Constanza Alejandro Emma Antonio Felipe'
print(usuarios)

#Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.#
time.sleep(2)
if 'Emma' in usuarios:
    print('Emma Existe')
time.sleep(2)
if 'Jorge' in usuarios:
    print('Jorge Existe') 
time.sleep(2)
if 'Felipe' in usuarios:
    print('Felipe Existe') 
           

#¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente su nombre? ¿Cómo solucionarías este problema?#

#No entiendo la pregunta. Dado que los nombres están en un string no veo como una persona podría buscar por nombre. Lo ideal sería transformarlo en una lista y ocupar if/else para buscar usuario.# 

#Convierte tu string en una lista, en la cual cada elemento es un usuario.#
time.sleep(2)
output=usuarios.split(' ')
print(output)

#Imprima en pantalla la cantidad usuarios que tiene tu aplicación#Hola
time.sleep(2)
numeropalabras = len(output)
print(numeropalabras)

#Imprima en pantalla un mensaje de saludo a los diferentes usuarios. 
# ¿Qué técnica puedes utilizar Imprima en pantalla un mensaje de saludo a los diferentes usuarios.#
#Se le pide al usuario que ingrese su nombre mediante input y se usa función print con el input más mensaje#
time.sleep(2)
nombre = input('Cual es tu nombre? ')
print('Hola' + ' ' + nombre +' '+ 'Te deseamos la mejor de las suertes')