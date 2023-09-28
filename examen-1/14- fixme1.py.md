## Objetivo
Obtener la bandera haciendo la correccion de sintaxis del archivo de python fixme
## Solución
```
octa143-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/25/fixme1.py
--2023-09-27 22:13:24--  https://artifacts.picoctf.net/c/25/fixme1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.71, 3.160.5.93, 3.160.5.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.71|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 837 [application/octet-stream]
Saving to: 'fixme1.py'

fixme1.py                                                           100%[=================================================================================================================================================================>]     837  --.-KB/s    in 0s      

2023-09-27 22:13:24 (381 MB/s) - 'fixme1.py' saved [837/837]

octa143-picoctf@webshell:~$ ls
Addadshashanammu  Addadshashanammu.zip  README.txt  code.py  codebook.txt  convertme.py  file  file.1  fixme1.py  static  warm
octa143-picoctf@webshell:~$ python fixme1.py 
  File "/home/octa143-picoctf/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
octa143-picoctf@webshell:~$ nano fixme1.py 
octa143-picoctf@webshell:~$ python fixme1.py 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_6a476c8f}
El archivo tenia una indentacion incorrecta, simplemente borrar unos espacios en la linea del print.
```
## Notas adicionales
## Referencias