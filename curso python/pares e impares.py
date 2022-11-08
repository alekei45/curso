#identificar pares e impares continue y break
n1= int(input("ingresa un numero: "))
n2=int(input("ingresa un numero mayo o igual:"))

if n2<n1:
    print("ingrese otro valor")
else:
    for i in range(n1,n2+1):

        if i% 2==0:
            print("el numero es par",i)
        else:
            print("el numero es impar",i)
        