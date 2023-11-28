## Objetivo

## Solución
```
Los bloques estan rotados en bloques de tres(por ejemplo, la cadena
the(0,1,2) seria het(1,2,0)), para resolver esto hice un pequeño script en
python que quedo asi
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
siendo la bandera picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}
```
## Notas adicionales
## Referencias
