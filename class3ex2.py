def leeAgenda(nombreFichero):
    archivo = open(nombreFichero,'r', encoding='utf8')
    lineas = archivo.readlines()
    n=1
    diccionario = {}
    diccionario.update(archivo)
    print(diccionario)