## Objetivo
Obtener la bandera con uso de jwt y las cookies

## Solución
```
Aqui se nos introduce los jwt, que son formas compactas para intercambiar informacion en paquetes json de manera mas segura, para acceder a la pagina como admin agarramos la cookie y lo llevamos a la pagina jwt.io, la cual al ponerla nos dara el json que podemos modificar, cambiamos el usuario a admin, y ahora el siguiente problema es que tenemos que encontrar una contraseña que no tenemos pistas sobre ella, para eso utilizamos un archivo llamado  rockyou.txt el cual contiene muchas contraseñas comunes, y el programa john al cual el damos el archivo rockyou y lo que hace es utilizar la cookie que le dimos y analiza si utiliza alguna contraseña de nuestro diccionario, en este caso si, es  ilovepico, cambiamos el paquete json y le ingresamos la contraseña y cambiamos la cookie por la nueva generada, dejandonos entrar como admin y dandonos la bandera, la cual es picoCTF{jawt_was_just_what_you_thought_f859ab2f}
```
## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=oiZk0tIkR48&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=11
https://jwt.io/