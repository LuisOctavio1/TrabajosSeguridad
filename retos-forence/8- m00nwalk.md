## Objetivo
Obtener la bandera de un archivo que aparentemente es de audio

## Solución
```
En este reto se nos enseña que hay un formato llamado sstv, el cual es una forma de mandar imagenes en formato de audo, instalamos un decodificador de sstv de github, utilizamos este decodificador con un comando el cual es 
sstv -d message.wav -o result.png
y nos da una imagen con la bandera que es:
picoCTF{beep_boop_im_in_space}
```
## Notas adicionales
## Referencias
https://github.com/colaclanth/sstv
https://www.youtube.com/watch?v=UyLTEpAz6eE&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=19