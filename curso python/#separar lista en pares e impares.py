#separar lista en pares e impares
ejemplo=[3,8,5,1,34,3,5,7,9,12]

def separar_lista(lista):
    lista.sort()
    pares=[]
    impares=[]

    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares
pares,impares =separar_lista(ejemplo)
print(pares)
print(impares)