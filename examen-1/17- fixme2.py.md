## Objetivo
Corregir el codigo python de fixme2 
## Datos de acceso al nivel
## Solución
```
octa143-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/6/fixme2.py
--2023-09-27 23:04:31--  https://artifacts.picoctf.net/c/6/fixme2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.71, 3.160.5.18, 3.160.5.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.71|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1029 (1.0K) [application/octet-stream]
Saving to: 'fixme2.py'

fixme2.py                                                           100%[=================================================================================================================================================================>]   1.00K  --.-KB/s    in 0s      

2023-09-27 23:04:31 (44.5 MB/s) - 'fixme2.py' saved [1029/1029]

octa143-picoctf@webshell:~$ python fixme2.py
  File "/home/octa143-picoctf/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
octa143-picoctf@webshell:~$ nano fixme2.py
octa143-picoctf@webshell:~$ python fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
```
## Notas adicionales
## Referencias