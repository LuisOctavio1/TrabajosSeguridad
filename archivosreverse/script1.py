with open("message.txt") as archivo:
    encriptado = archivo.read()
bandera = ""
for i in range(0,len(encriptado)):
    if((i+1)%3 ==0 and (i!=1 and i != 0)):
        letraRotada = encriptado[i]
        bandera += letraRotada
        bandera += encriptado[i-2]
        bandera += encriptado[i-1]
print(bandera)

    
    
