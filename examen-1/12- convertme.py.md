## Objetivo
Ejecutar un script de python y darle el numero 37 en binario

## Solución
```
octa143-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/23/convertme.py
--2023-09-27 17:08:38--  https://artifacts.picoctf.net/c/23/convertme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.93, 3.160.5.71, 3.160.5.42, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.93|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1189 (1.2K) [application/octet-stream]
Saving to: 'convertme.py'

convertme.py                                               100%[=======================================================================================================================================>]   1.16K  --.-KB/s    in 0s      

2023-09-27 17:08:38 (46.0 MB/s) - 'convertme.py' saved [1189/1189]

octa143-picoctf@webshell:~$ python convertme.py 
If 37 is in decimal base, what is it in binary base?
Answer: 100101
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_9c3b7d4d}
```
## Notas adicionales
## Referencias
https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)To_Binary('Space',2)&input=Mzc