import class3ex1
import class3ex2
#IMPORTANTE, ESTE PROGRAMA SOLO ENCUENTRA LA PRIMERA COINCIDENCIA, SE PODRÍA HACER DE FORMA RECURSIVA LLAMANDO A UN PUNTO EN EL
#QUE SE REPITA EL BUCLE QUE BUSCA, PERO BUSCANDO SOBRE UNA LISTA ELIMINANDO LA ANTERIOR COINCIDENCIA
n=int(input('¿De cuántos contactos quiere que sea la agenda?'))
class3ex1.creaAgenda('agenda', n)
diccionario = class3ex2.leeAgenda('agenda.csv')
print('Bienvenido a tu agenda de contactos') #Lo ponemos aqui para que si dan una opción no válida no se vuelva a imprimir la cabecera
def agendaContactos():
    open('agenda.csv','r') #Abrimos la agenda que hemos creado antes, la hemos creado fuera de al función para no crear nuevas cada vez que la invocamos
    print('--------------------------------------')
    print('Escriba 1 para consultar el número de teléfono de uno de sus contactos')
    print('Escriba 2 para salir del programa')
    opcion = int(input()) #Lo pasamos a int para que no haya problemas con los operadores lógicos
    if opcion == 1:
        nombre = input('Dígame la persona cuyo número quiere saber').lower() #Se tiene que pasar a minúscula para la búsqueda
        lista = list(diccionario) #Pasamos el diccionario a una lista para poder hacer una búsqueda sobre todas las entradas de forma ordenada
        encontrado = False #En un principio no se ha encontrado
        i=0
        while encontrado==False and i <= len(lista)-1:#Mientras que no se encuentre y no nos pasemos de largo se sigue buscando
            if (lista[i].lower()).find(nombre) != -1: #Recorremos toda la lista y buscamos la cadena en cada uno de los string de cada posición de la lista
                posicion = i #Guardamos la posición en la que estaba
                encontrado = True
            i += 1
        if encontrado == False: #En caso de recorrer toda la lista y no encontrar coincidencias
            print('Lo sentimos, esa persona no está en esta agenda de contactos')
        else:
            print('Se ha encontrado una coincidencia!')
            print(diccionario[str(lista[i])]) #Aqui le pasamos la posición encontrada a la lista, de ahi extraemos la clave, y se la pasamos al diciconario
    elif opcion == 2:
        exit()
    else:
        print('Esa opción no es válida!')
        agendaContactos()
agendaContactos()
