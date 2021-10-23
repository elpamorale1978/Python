import time

usuarios = {}

while True:
    nombre = input("Ingrese su nombre: ")
    print("----------------------------")
    contrasena = input("Ingrese alguna contraseña: ")
    print("----------------------------")
    usuarios[nombre] = contrasena
    edad = int(input("Ingrese su edad: "))
    print("----------------------------")
    usuarios[nombre] = contrasena, edad

    for keys, values in usuarios.items():
        time.sleep(5)
        print("Nombre:", keys, "Contraseña:", values[0], "Edad: ", values[1])

    pregunta = input("Desea Salir (Si/No): ")
    if pregunta == "Si":
        break
    else:
        continue

print(usuarios)