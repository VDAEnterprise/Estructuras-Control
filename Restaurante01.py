#Entrada de datos
print("Descuento del Restaurante")
p = float(input("ingrese cantidad a pagar: "))
#Proceso
print("="*30)
print("----- Factura de Consumo -----")
if p >= 0 :
    if p <= 100:
        #descuento del 10%
            print("Usted a ganado el 10% de descuento")
            d = p * 0.10 
        #descuento del 20%   
    elif p <= 200:
        print("Usted a ganado el 20% de Descuento")
        d = p * 0.20
        
    else:
        #descuento 30%
        d = p * 0.30
        print("Usted a ganado el 30% de Descuento")
        
    #Monto con Descuento
    Md = p-d  
    #impuesto
    i = (p - d) * 0.19 
    #Importe apagar
    ip = (p-d)+i     
    #salida(Resultado)  
    print("="*30)
    print("="*30)
    print("Consumo: ",p)
    print("Descuento: ",d)
    print("Monto con Descueto: ",Md)
    print("El Impuesto es: ",i)
    print("Importe a Pagar: ",ip)
    print("="*30)
    print("----- Gracias por su Compra -----")
    print("----------Vuelva Pronto----------")
    print("="*30)
else:
    print("Error de Pago")    




    

    
