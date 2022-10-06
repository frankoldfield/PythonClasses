def leeAgenda(NombreFichero):
    archivo = open(NombreFichero,'rt')
    lineas = archivo.readlines()
    n=1
    agenda = {}
    while l:
        campos = l.split(";")
        nombre = campos[0]
        tlf = campos[1].strip()
        if not agenda.get(nombre):
            agenda[nombre]=[tlf]
        else
            agenda[nombre].append(tlf)
            print()
        archivo=readline.f
        archivo.close()
        #nuevaentrada = nuevaentrada.split(sep=';') #Aquí dividimos los campos a introducir en el diccionario
        #nuevaentrada = nuevaentrada.split(sep=';')
        #agenda[nuevaentrada[0]]=(nuevaentrada[1:]) #Como split devuelve una lista de cadenas, tenemos que coger la posición 0 para el nombre y las demás para los números
        #print(diccionario['Alejandro Ruíz Sánchez']) #Este print son para comprobar que se han introducido bien los datos
        n += 1
    return agenda
leeAgenda('Prueba.csv')
