#mostrar suma del 1 al 6
N =int(input("ingresa un numero"))

suma=0
i=1
while i<=N:
    suma=suma + i
    i=i+1
print ("la suma de los numeros hastas el", N,"es: ",suma)