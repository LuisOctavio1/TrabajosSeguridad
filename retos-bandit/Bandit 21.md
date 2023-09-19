# Level 21
## Objetivo
Encontrar la contraseña en un programa que se esta ejecutando programadamente
## Datos de acceso al nivel
bandit21@bandit.labs.overthewire.org
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
## Solución
```
bandit21@bandit:~$ ls -la /etc/cron.d
total 56
drwxr-xr-x   2 root root  4096 Apr 23 18:05 .
drwxr-xr-x 108 root root 12288 Aug 12 08:42 ..
-rw-r--r--   1 root root    62 Apr 23 18:04 cronjob_bandit15_root
-rw-r--r--   1 root root    62 Apr 23 18:04 cronjob_bandit17_root
-rw-r--r--   1 root root   120 Apr 23 18:04 cronjob_bandit22
-rw-r--r--   1 root root   122 Apr 23 18:04 cronjob_bandit23
-rw-r--r--   1 root root   120 Apr 23 18:04 cronjob_bandit24
-rw-r--r--   1 root root    62 Apr 23 18:04 cronjob_bandit25_root
-rw-r--r--   1 root root   201 Jan  8  2022 e2scrub_all
-rwx------   1 root root    52 Apr 23 18:05 otw-tmp-dir
-rw-r--r--   1 root root   102 Mar 23  2022 .placeholder
-rw-r--r--   1 root root   396 Feb  2  2021 sysstat
bandit21@bandit:~$ ls /etc/cron.d
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24       e2scrub_all  sysstat
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root  otw-tmp-dir
bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff
```
## Notas adicionales
Lo que hacemos  es primero ver todo los que esta en la carpeta  de cron (los programas que están programados), se puede ver que no hay uno para el usuario 21, luego vemos lo que hace el archivo bandit22.sh, lo cual abre un archivo en cierta ruta, el cual podemos acceder desde nuestro usuario, así que hacemos un cat a esa ruta y a ese archivo y nos da la contraseña
## Referencias