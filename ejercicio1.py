#Dado 3 numeros, devolver los numeros en orden ascendente
print("Digite Tres Numeros")
n1=int(input("digite primer numero: "))
n2=int(input("digite segundo numero: "))
n3=int(input("digite tercer numero: "))

if n1 > n2 and n3:
    mayor = n1
else:
    if n2 > n1 and n3:
        mayor = n2
    else:
        mayor = n3
if n1 < n2 and n3:
    menor = n1
else:
    if n2 < n1 and n3:
        menor = n2
    else:
        menor = n3
        
intermedio = (n1+n2+n3)-(mayor-menor) 

print (mayor)
print(intermedio)
print(menor)
        


    

    


    




     
    