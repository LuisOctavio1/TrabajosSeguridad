# Level X

## Objetivo
El objetivo de este reto es obtener la contraseña de un archivo data.txt que esta en codigo base64
## Datos de acceso al nivel
**bandit10@bandit.labs.overthewire.org**
G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
## Solución
PS C:\Users\PC\.ssh> ssh bandit10@bandit.labs.overthewire.org -p 2220

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us on discord or IRC.

  Enjoy your stay!

bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt  
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==  
bandit10@bandit:~$ cat data.txt | base64 -d  
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM  

## Notas adicionales
Lo primero que se hace es ver el contenido del archivo data con cat, esta en base 64 como se indico en el problema, asi que utilizamos el comando cat data.txt concatenado con el comando base64 -d, el cual decodifica codigo base 64 y da el resultado como salida, dando la contraseña
## Referencias