#continue
n=int(input("ingresa un numero"))
for i in range(1,n+1):
    if i %2==0:
        continue#salta a la siguiente instruccion(que no sea par)

        print("el numero: ",i,"es par")
    else:
        print("el numero ",i,"es inpar")