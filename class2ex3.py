def programausuario2():
    print('A continuación tiene que proporcionarme dos cadenas, y le diré cuántas veces aparece la primera en la segunda, y en qué posición aparece cada una de esas veces')
    sub = input()
    cad = input()
    num = cad.count(sub)
    cont = 0
    pos = cad.find(sub)
    while cont < num:
        print('Aparece una vez en',pos)
        pos = cad.find(sub,pos+1)#El 1 es para que omita el inicio de esta coincidencia, si no se queda atascado
        cont += 1
programausuario2()







    #primero buscamos la cadena, con las posiciones de inicio y de fin, a continuación, separamos por la izquierda la cadena hasta el inicio de la contenida
    #y por la derecha desde el final de la contenida hasta el final de la cadena contenedora, ahora juntamos esas dos separaciones, e iteramos