# Level 14
## Objetivo
Conectarse al puerto 30000 con nc dándole la contraseña de este nivel para obtener la nueva contraseña
## Datos de acceso al nivel
**bandit14@bandit.labs.overthewire.org**
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
## Solución
```
bandit14@bandit:~$ ls  
bandit14@bandit:~$ nc localhost 30000  
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq  
Correct!  
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt  
```
## Notas adicionales
Se conecta al puerto 30000 con el comando nc y se le da la contraseña actual como se indica, dando como salida la contraseña del siguiente nivel
## Referencias