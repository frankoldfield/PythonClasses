import random

def creaAgenda(nombreFichero, n):
    lista_nombres = ['Antonio', 'Alfonso', 'Eugenio', 'Evaristo', 'Pablo', 'Alberto', 'Alejandro', 'Laura', 'Estela', 'Rosa']
    lista_apellidos = ['Martínez', 'Morales', 'Marín', 'López', 'García', 'Zapata', 'Gómez', 'Ruíz', 'Sánchez', 'Chicote']
    archivo = open(nombreFichero+'.csv', 'w', encoding='utf8')
    ini = 100000000
    fin = 999999999
    for i in range (0,n,1):
        entrada = lista_nombres[random.randint(0, 9)]+' '
        entrada += lista_apellidos[random.randint(0, 9)]+' '
        entrada += lista_apellidos[random.randint(0, 9)]
        entrada += ';'+str(random.randint(ini,fin)) #Importante hacer el casting, si no no puede concatenar con el +=
        archivo.write('<'+entrada+'>\n') #Normálmente se pueden concatenar Strings con la coma, pero como .write es una función
CreaAgenda('Prueba', 7)                #que toma parámetros, la , se toma como una separación de parámetros, asi que tenemos que concatenarlos con el +
#Puede ser que la función que crea un string tome varios parámetros separados con la , y los concatena, y en realidad eso es lo que está pasando cuando concatenamos con las comas?
