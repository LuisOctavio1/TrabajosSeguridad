## Objetivo

## Solución
```
Se nos dice que nos daran una archivo con varios numeros los cuales para
desencriptar tenemos que hacerles modulo 37, en caso de el resultado sea del
0 al 35 es una letra en mayuscula, del 26 al 35 numeros y 37 _, el codigo
para hacerlo quedo de la siguiente manera
datos = open('message.txt').read().split()

bandera = ""

for i in datos:

    modu = int(i) % 37

    if modu >= 0 and modu <=25:

        bandera += chr(modu+65)

    elif modu >=26 and modu<=35:

        bandera += chr(modu+22)

    else:

        bandera+= '_'

  

print("picoCTF{" + bandera + "}")
siendo la bandera picoCTF{R0UND_N_R0UND_79C18FB3}
```
## Notas adicionales
## Referencias