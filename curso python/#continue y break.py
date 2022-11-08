#continue y break
#separarb los numero y terminar el programa al encontar el primer numero divisible por 6
n=int(input("ingresa un numero"))
for i in range(1,n+1):
    if i%2==0:
        continue
        print(i)     
    else:
        print(i)
    if i%6==0:
        break


        
    
