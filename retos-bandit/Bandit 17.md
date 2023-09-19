# Level 17
## Objetivo
Encontrar la contraseña nueva que se encuentra en un archivo password.new, comparándolo con el password.old
## Datos de acceso al nivel
ssh -i .\contra.txt bandit17@bandit.labs.overthewire.org -p 22
contra.txt (llave que nos dieron el reto pasado)
## Solución
```
bandit17@bandit:~$ ls -la
total 36
drwxr-xr-x  3 root     root     4096 Apr 23 18:04 .
drwxr-xr-x 70 root     root     4096 Apr 23 18:05 ..
-rw-r-----  1 bandit17 bandit17   33 Apr 23 18:04 .bandit16.password
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit18 bandit17 3300 Apr 23 18:04 passwords.new
-rw-r-----  1 bandit18 bandit17 3300 Apr 23 18:04 passwords.old
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
drwxr-xr-x  2 root     root     4096 Apr 23 18:04 .ssh
bandit17@bandit:~$ diff passwords.old passwords.new --color
42c42
< glZreTEH1V3cGKL6g4conYqZqaEj0mte
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
```
## Notas adicionales
Primero, se tuvo que acceder a este servidor mediante la llave ssh de la pasada, la cual esta en un archivo notas al que le tuve que modificar los accesos de los demás usuarios (esto lo hice de manera visual desde la parte de propiedades de windows), una vez dentro desplegamos todos los archivos para confirmar que estén ahí, luego con el comando diff le decimos que nos de la diferencia de los dos archivos y con el ---color que les ponga un color distinto, dándonos la contraseña del siguiente nivel
## Referencias