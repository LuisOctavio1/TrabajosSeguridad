## Objetivo

## Solución
```
Aqui lo que tenemos un archivo con espacios en blanco con caracteres unicode en utf8, los cuales asumimos con son 0 y 1, con el siguiente script los reemplazamos y imprimimos la bandera.
from pwn import *

file = open('whitepages.txt', 'rb')
data = bytearray(file.read())
data = data.replace(b'\xe2\x80\x83',b'0')
data = data.replace(b'\x20',b'1')
data = data.decode('ascii')
data = unbits(data)

print(data)

picoCTF{not_all_spaces_are_created_equal_c54f27cd05c2189f8147cc6f5deb2e56}
```
## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=427HDV7tzow&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=20