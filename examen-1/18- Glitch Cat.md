## Objetivo
Encontrar la llave entrando en un servidor, el cual indica que esta bugueado y que no imprime bien la contraseña

## Solución
```
octa143-picoctf@webshell:~$ nc saturn.picoctf.net 49700
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
^C   
octa143-picoctf@webshell:~$ touch programa.py
octa143-picoctf@webshell:~$ nano programa.py 
octa143-picoctf@webshell:~$ python programa.py 
picoCTF{gl17ch_m3_n07_a4392d2e}
```
## Notas adicionales
se crea un archivo llamado programa.py donde el codigo es print('picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'), dando la contraseña de manera correcta.
## Referencias