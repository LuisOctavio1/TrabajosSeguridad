## Objetivo
obtener la bandera de un archivo de captura de paquetes

## Solución
```
Analizando los paquetes de UDP podemos ver unas pistas, las cuales son que en un stream marca incio y en otro final los cuales comparten el puerto destino 22, analizando solo los paquetes udp que tienen el puerto 22 como destino, vemos que practicamente todos tienen como inicio el puesto 5000 o menos de 6000, haciendo una resta de 5000 menos el puerto, obtenemos el codigo ascii de una letra de la bandera, para automatizar todo, hacemos un script en python el cual es el siguiente
from scapy.all import *

packets = rdpcap('capture.pcap')
print(packets)

flag = ''

for p in packets:
    if UDP in p and p[UDP].dport ==22:
        if p[UDP].sport >5000: 
            flag += chr(p[UDP].sport - 5000)

print(flag)

El cual obtiene los paquetes, luego revisa que esten en udp y su puerto destino sea 22, despues si el purto de inicio es mayor que 5000, al puerto le restamos 5000 y esto lo combertimos a caracter con la funcion chr, y luego se la sumamos a una cadena llamada flag, asi obtenemos la bandera la cual es 
picoCTF{p1LLf3r3d_data_v1a_st3g0}

```

## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=WcMl1SvQ6hI&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=23