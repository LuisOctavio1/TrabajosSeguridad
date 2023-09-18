# Level 11

## Objetivo
El objetivo de este reto es obtener la contraseña de un archivo en el cual la contraseña estará en root 13.
## Datos de acceso al nivel
**bandit11@bandit.labs.overthewire.org**
6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
## Solución
```
PS C:\Users\PC> ssh bandit11@bandit.labs.overthewire.org -p 2220  
bandit11@bandit:~$ ls  
data.txt  
bandit11@bandit:~$ cat data.txt  
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi  
bandit11@bandit:~$ cat data.txt | tr [a-zA-Z] [n-za-mN-ZA-M]  
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv  
```
## Notas adicionales
Sabiendo que la contraseña esta en root 13, ósea que se rotan las letras 13 veces, lo que hacemos es utilizar el cat para mostrar el contenido, concatenado con el comando tr, el cual cambia las cosas que le ponemos al principio por las del final, en este caso la n en z y la a en m, al igual que con las mayúsculas.
## Referencias