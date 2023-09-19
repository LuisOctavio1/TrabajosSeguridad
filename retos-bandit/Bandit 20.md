# Level 20
## Objetivo
Mandarle la contraseña a un puerto y recogerla con el archivo suconnect para que nos de la contraseña
## Datos de acceso al nivel
bandit20@bandit.labs.overthewire.org
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
## Solución
```
bandit20@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Apr 23 18:04 .
drwxr-xr-x 70 root     root      4096 Apr 23 18:05 ..
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
-rwsr-x---  1 bandit21 bandit20 15600 Apr 23 18:04 suconnect
bandit20@bandit:~$ ./suconnect  5050
Could not connect
bandit20@bandit:~$ nc -lnvp 5050 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Listening on 0.0.0.0 5050
^C
bandit20@bandit:~$ nc -lnvp 5050 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[1] 1801866
bandit20@bandit:~$ Listening on 0.0.0.0 5050

bandit20@bandit:~$ ./suconnect 5050
Connection received on 127.0.0.1 51714
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
```
## Notas adicionales
Primero verificamos los archivos, luego enviamos al puerto 5050 la contraseña y & al final para indicar que sea en segundo plano, después abrimos el archivo con el puerto 5050 para así darle la contraseña que le dimos al puerto y obtener la nueva
## Referencias