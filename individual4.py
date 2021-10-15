# #Opcion1
usuario = input("Ingrese su Nombre: ")
contrasena = input("Favor crear contraseña (Mínimo 8 caracteres con mayuscula, minuscula y al menos un digito): ")

largo = len(contrasena)
if largo < 8:
    print("Contraseña debe tener al menos 8 caracteres")

mayuscula=False 
minuscula=False 
numeros=False 

for caracteres in contrasena: 
    if caracteres.isupper()== True: 
        mayuscula=True                 
    if caracteres.islower()== True:
        minuscula=True             
    if caracteres.isdigit()== True:
        numeros=True 

if mayuscula == True and minuscula == True and numeros == True:
    print("Contraseña cumple con los requisitos")
else: 
    print("Contraseña debe incluir mayúsculas, minúsculas y un numero")

#Opcion2

import random
import time

lista = ["Hábitos alimenticios", "Experiencia laboral", "Actividades recreativas", "Atletismo", "Natación", "Deportes en general"]
contador = 0

print("Encuestas a completar")

while contador < 7:
    nuevalista = random.sample(lista,5)
    separator = ", "
    time.sleep(3)
    print ("Usuario", contador + 1, ":", separator.join(nuevalista))
    contador = contador + 1
time.sleep(2)
print("Fin de asignación de encuestas")