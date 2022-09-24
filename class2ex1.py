def potencia(cadena, n):
    return  n*cadena

def refleja(cadena):
    return cadena[::-1]

def prefijo(cadena,pre):
    return cadena.startswith(pre)

def sufijo(cadena,suf):
    return cadena.endswith(suf)


def subcadena(cadena,sub):
    return sub in cadena