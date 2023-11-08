## Objetivo

## Solución
```
Para este reto, lo primero que tuve que hacer fue utilizar un comando 
llamado steghide para extraer el texto ecnriptado a desencriptar,
depues con el texto que es krxlXGU{zgyzhs_xizxp_8z0uvwwx} y con la imagen se
puede desencriptar facilmente, el codigo en python seria asi:
datos = open('encrypted.txt').read()

bandera = ""

for i in datos:

    if 'a' <= i <= 'z':

        bandera+= chr(122 - (ord(i) - 97))

    elif 'A' <= i <= 'Z':

        bandera+= chr(90 - (ord(i) - 65))

    else:

        bandera+=i

  

print(bandera)
dando la bandera picoCTF{atbash_crack_8a0feddc}
```
## Notas adicionales
## Referencias