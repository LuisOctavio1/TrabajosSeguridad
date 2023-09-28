## Objetivo
obtener la llave de un script de python
## Solución
```
octa143-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/2/code.py
--2023-09-27 17:06:05--  https://artifacts.picoctf.net/c/2/code.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.93, 3.160.5.42, 3.160.5.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.93|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1278 (1.2K) [application/octet-stream]
Saving to: 'code.py'

code.py                                                    100%[=======================================================================================================================================>]   1.25K  --.-KB/s    in 0s      

2023-09-27 17:06:06 (48.9 MB/s) - 'code.py' saved [1278/1278]

octa143-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/2/codebook.txt
--2023-09-27 17:06:15--  https://artifacts.picoctf.net/c/2/codebook.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.42, 3.160.5.18, 3.160.5.93, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27 [application/octet-stream]
Saving to: 'codebook.txt'

codebook.txt                                               100%[=======================================================================================================================================>]      27  --.-KB/s    in 0s      

2023-09-27 17:06:15 (15.0 MB/s) - 'codebook.txt' saved [27/27]

octa143-picoctf@webshell:~$ ls
Addadshashanammu  Addadshashanammu.zip  README.txt  code.py  codebook.txt  static  warm
octa143-picoctf@webshell:~$ chmod +x code.py 
octa143-picoctf@webshell:~$ ./code.py 
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/346.
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/346.
./code.py: line 7: syntax error near unexpected token `('
./code.py: line 7: `def str_xor(secret, key):'
octa143-picoctf@webshell:~$ python code.py 
picoCTF{c0d3b00k_455157_7d102d7a}
octa143-picoctf@webshell:~$ 
```
## Notas adicionales
## Referencias