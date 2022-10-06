import random

def creaAgenda(nombreFichero, n):
    lista_nombres = ['Antonio', 'Alfonso', 'Eugenio', 'Evaristo', 'Pablo', 'Alberto', 'Alejandro', 'Laura', 'Estela', 'Rosa']
    lista_apellidos = ['Martínez', 'Morales', 'Marín', 'López', 'García', 'Zapata', 'Gómez', 'Ruíz', 'Sánchez', 'Chicote']
    archivo = open(nombreFichero+'.csv', 'w', encoding='utf8')
    for i in range (0,n,1):
        entrada = random.choice(lista_nombre)+' '
        entrada += random.choice(lista_apellido)+' '
        entrada += random.choice(lista_apellido)
        entrada += ';'+("%09d" % random.randint(0,999999999)) #Importante hacer el casting, si no no puede concatenar con el += UTILIZAMOS %09d COMO EN C PARA RELLENAR LA CADENA DEL TLF
        archivo.write('<'+entrada+'>\n') #Normálmente se pueden concatenar Strings con la coma, pero como .write es una función
creaAgenda('Prueba', 7)                #que toma parámetros, la , se toma como una separación de parámetros, asi que tenemos que concatenarlos con el +
#Puede ser que la función que crea un string tome varios parámetros separados con la , y los concatena, y en realidad eso es lo que está pasando cuando concatenamos con las comas?
