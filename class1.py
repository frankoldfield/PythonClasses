def segundos(years):
    return(years*365*24*3600)
print(segundos(2000))

def par(num):
    return num%2 == 0
print(par(7))
print(par(8))

def primo(num2):
    i=2
    prime = True
    while(i<=(num2+1)//2):
        if(num2%i==0):
            prime = False
        i+=1
    print(num2, prime)
primo(997)

def primohasta(lim):
    primo2=1
    while (primo2 <= lim):
        primo(primo2)
        primo2+=1
print(primohasta(1000))