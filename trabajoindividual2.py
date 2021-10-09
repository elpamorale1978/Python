#Se crea la variable usuarios con el nombre de 7 usuarios. Variable tipo String#

usuarios = 'Jorge Manuel Constanza Alejandro Emma Antonio Felipe'
print(usuarios)

#Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.#
#Se imprimen los nombres de 3 usuarios encontrando los caracteres de sus nombre en el string#

print(usuarios[0:5])
print(usuarios[13:22])
print(usuarios[33:37])

#¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente su nombre? ¿Cómo solucionarías este problema?#

#No entiendo la pregunta. Dado que los nombres están en un string no veo como una persona podría buscar por nombre. Lo ideal sería transformarlo en una lista y ocupar la función index.# 

#Convierte tu string en una lista, en la cual cada elemento es un usuario.#

output=usuarios.split(' ')
print(output)

#Imprima en pantalla la cantidad usuarios que tiene tu aplicación#Hola
numeropalabras = len(output)
print(numeropalabras)

#Imprima en pantalla un mensaje de saludo a los diferentes usuarios. 
# ¿Qué técnica puedes utilizar Imprima en pantalla un mensaje de saludo a los diferentes usuarios.#
#Se le pide al usuario que ingrese su nombre mediante input y se usa función print con el input más mensaje#

nombre = input('Cual es tu nombre? ')
print('Hola' + ' ' + nombre +' '+ 'Te deseamos la mejor de las suertes')