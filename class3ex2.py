def leeAgenda(NombreFichero):
    archivo = open(NombreFichero,'r')
    lineas = archivo.readlines()
    n=1
    diccionario = {}
    for linea in lineas:
        nuevaentrada = linea.strip('<>\n') #Aquí le quitamos los caracteres indicados
        nuevaentrada = nuevaentrada.split(sep=';') #Aquí dividimos los campos a introducir en el diccionario
        diccionario[nuevaentrada[0]]=(nuevaentrada[1:]) #Como split devuelve una lista de cadenas, tenemos que coger la posición 0 para el nombre y las demás para los números
        #print(diccionario['Alejandro Ruíz Sánchez']) #Este print son para comprobar que se han introducido bien los datos
        n += 1
    return diccionario
leeAgenda('Prueba.csv')