#for
frase=str(input("ingrese una frase :"))
vocales="aeiouAEIOU"
contador=0
for i in frase:
    if i in  vocales:
        contador=contador+1
print("el numero de vocales es: ",contador)