import class2ex1


def programausuario():
    print('Elija a qué función quiere acceder')
    print('1 - potencia\n2 - refleja \n3 - prefijo\n4 - sufijo\n5 - subcadena')

    opcion = input()

    if opcion == '1':
        print('Elija primero la palabra y después el número de veces que quiere que se repita la palabra')
        cadena = input()
        n = int(input())
        print(class2ex1.potencia(cadena,n))
    elif opcion == '2':
        print('Elija primero la palabra a reflejar')
        cadena = input()
        print(class2ex1.refleja(cadena))
    elif opcion == '3':
        print('Elija primero la palabra y después el prefijo')
        cadena = input()
        n = input()
        print(class2ex1.prefijo(cadena, n))
    elif opcion == '4':
        print('Elija primero la palabra y después el sufijo')
        cadena = input()
        n = input()
        print(class2ex1.sufijo(cadena, n))
    elif opcion == '5':
        print('Elija primero la palabra y después la subcadena')
        cadena = input()
        n = input()
        print(class2ex1.subcadena(cadena, n))

    else:
        print('Esa opción no es válida!')
        programausuario()
programausuario()