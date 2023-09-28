## Objetivo
Obtener la bandera ejecutando el script runme
## Solución
```
octa143-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/34/runme.py
--2023-09-28 04:22:01--  https://artifacts.picoctf.net/c/34/runme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.93, 3.160.5.71, 3.160.5.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.93|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'runme.py'

runme.py                                                            100%[=================================================================================================================================================================>]     270  --.-KB/s    in 0s      

2023-09-28 04:22:01 (5.53 MB/s) - 'runme.py' saved [270/270]

octa143-picoctf@webshell:~$ python runme.py 
picoCTF{run_s4n1ty_run}
```
## Notas adicionales
## Referencias