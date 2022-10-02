def leeAgenda(NombreFichero):
    archivo = open(NombreFichero,'r')
    lineas = archivo.readlines()
    n=1
    diccionario = {}
    for linea in lineas:
        nuevaentrada = linea.strip('<>\n') #Aquí le quitamos los caracteres indicados
        nuevaentrada = nuevaentrada.split(sep=';') #Aquí dividimos los campos a introducir en el diccionario
        diccionario['nombre'+str(n)]=(nuevaentrada[0]) #Como split devuelve una lista de cadenas, tenemos que coger la posición 0 para el nombre
        del nuevaentrada[0]#Aquí le estamos quitando la primera entrada a la lista de campos, para solo quedarnos con los números del contacto
        diccionario['numero' + str(n)] = (nuevaentrada) #Aqui le añadimos todos los campos restantes como números de teléfono
        print(diccionario['nombre'+str(n)]) #Estos print son para comprobar que se han introducido bien los datos
        print(diccionario['numero' + str(n)])
        n += 1
leeAgenda('Prueba.csv')