
N= float(input("ingresa tus notas: " ))
if N< 5.6:
    R="reprobado"
elif N <8.0:
    R="aprobado"
elif N < 9.0:
    R="sobresaliente"
else:
    R="exelente"
print("su nota",N,R)
