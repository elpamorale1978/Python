import time
# Diseñe 7 diccionarios, donde el nombre de cada diccionario es el nombre de un usuario de su aplicación.
Antonio = {}
Emma = {}
Pablo = {}
Felipe = {}
Constanza = {}
Ronald = {}
Emanuel = {}

# En cada diccionario, integre características como: edad, género y otras características particulares de su
# aplicación.Por ejemplo, si la aplicación se enfoca en Juntas de Vecinos integrar dirección y número telefónico.
# Integre al menos cinco características.
#Se agregan rut como identificador y los valores nombre, edad, genero, telefono, dirección
Antonio ['5.423.607-7'] = ['Antonio Morales', 20, "Masculino", "953973743", "Chusmiza 1821"]
Emma ['4.950.103-k'] = ['Emma Ortega', 65, "Femenino", "953748243", "Padre Mariano 87 Depto 1004"]
Pablo ['10.499.128-9'] = ['Pablo Morales', 43, "Masculino", "989674523", "Republica de Honduras 11888"]
Felipe ['10.499.129-7'] = ['Felipe Morales', 45, "Masculino", "913243546", "Curanipe 24"]
Constanza ['13.234.453-k'] = ['Constanza Hurtado', 32, "Femenino", "947562958", "Avenida Ossa 2345"]
Ronald ['11.243.546-9'] = ['Ronald Madariaga', 29, "Masculino", "924259674", "Chile Lindo 6745 Depto 14"]
Emanuel ['15.324.111-9'] = ['Emanuel Holguin', 32, "Masculino", "972942845", "Avenida Argentina Casa C"]

# Guarde estos diccionarios en una lista. En el caso de ejemplo, podría ser nombrada “JJVV”.
#superdiccionario = Se crea diccionario llamado superdiccionario agregando cada diccionario original usando **
superdiccionario = {**Antonio, **Emma, **Pablo, **Felipe, **Constanza, **Ronald, **Emanuel}

#lista = Se transforma el superdiccionario en lista usando list y items para que retorne clave y valor**
lista = list(superdiccionario.items())
print(type(lista))

# A continuación, recorra su lista e imprima toda la información que posee la estructura de datos sobre
# cada usuario (en el caso de ejemplo: de cada junta de vecinos).
time.sleep(2)
for x in lista: #Se utliza ciclo for para imprimir los valores de clave y valor de la lista.
    print("Información de casa Usuario", x)
print("**************************************************************************")

# ¿Qué problemas encontró con esta forma de almacenar la información?
#No parece logico incorporar información de distintos usuarios en distintos diccionario. Sería más lógico agregarlos en un solo diccionario

# Vuelva al inicio del problema y diseñe una estructura de datos unificada que permita almacenar todas
# las juntas de vecinos.
#Se crea diccionario llamado usuarios con toda la información

usuarios = {'5.423.607-7':['Antonio Morales', 20, "Masculino", "953973743", "Chusmiza 1821"],
                       '4.950.103-k':['Emma Ortega', 65, "Femenino", "953748243", "Padre Mariano 87 Depto 1004"],
                       '10.499.128-9':['Pablo Morales', 43, "Masculino", "989674523", "Republica de Honduras 11888"],
                       '10.499.129-7':['Felipe Morales', 45, "Masculino", "913243546", "Curanipe 24"],
                       '13.234.453-k':['Constanza Hurtado', 32, "Femenino", "947562958", "Avenida Ossa 2345"],
                       '11.243.546-9':['Ronald Madariaga', 29, "Masculino", "924259674", "Chile Lindo 6745 Depto 14"],
                       '15.324.111-9':['Emanuel Holguin', 32, "Masculino", "972942845", "Avenida Argentina Casa C"]     
                                                        }
time.sleep(2)
print(usuarios)
print("**************************************************************************")                                                        
# Agregue para cada usuario los campos nombre_usuario, id_unico, antigüedad, fecha de incorporación.
# Se agregan variables con listas de los elementos que hay que agregar. Se agregan al diccionario usando clave y extend

antonio = ["antonio1234", 1, 10, "10/10/2011"]
emma = ["emma4321", 2, 7, "07/02/2012"]
pablo = ["pamorale1978", 3, 1, "01/15/2021"]
felipe = ["feli_13", 4, 7, "22/06/2020"]
constanza = ["churtado44", 5, 7, "01/02/2019"]
ronald = ["ronald23", 6, 7, "30/11/2020"]
emanuel =["manu56", 7, 7, "18/08/2021"]

usuarios['5.423.607-7'].extend(antonio)
usuarios['4.950.103-k'].extend(emma)
usuarios['10.499.128-9'].extend(pablo)
usuarios['10.499.129-7'].extend(felipe)
usuarios['13.234.453-k'].extend(constanza)
usuarios['11.243.546-9'].extend(ronald)
usuarios['15.324.111-9'].extend(emanuel)

time.sleep(2)

for clave,valor in usuarios.items():
    print(clave, valor)

#print(usuarios)
# Imprima en pantalla la fecha de incorporación de todos los usuarios
 
time.sleep(2)

for clave,valor in usuarios.items():
    print("Usuario", clave, "Fecha Incorporacion", valor[-1])