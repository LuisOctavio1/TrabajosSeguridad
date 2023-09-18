# Level 13
## Objetivo
Utilizar el comando ssh para ingresar una llave privada y poder acceder a la contraseña del usuario 14

## Datos de acceso al nivel
**bandit13@bandit.labs.overthewire.org**
wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
## Solución
```
bandit13@bandit:~$ ls  
sshkey.private  
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost -p 2220  
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14  
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq  
bandit14@bandit:~$ exit  
logout  
Connection to localhost closed.  
```
## Notas adicionales
Lo que hacemos aquí es ver que tenemos una llave  para conectarnos vía ssh a un servidor como el usuario 14, lo que hacemos es poner el comando ssh -i que indica que le daremos una llave, y una vez ahí indicamos que nos de la llave para acceder al reto 14. 
## Referencias