## Objetivo
Encontrar la bandera en un archivo txt

## Solución
```
Aqui se nos muestra que aunque un archivo sea txt, puede que enrealidad sea de otro tipo, en este caso podemos comprobarlo mediante el comando file, al hacerlo podemos comprobar que en realidad es un archivo png, con lo cual hacemos un mv en la misma carpeta y con eso le cambiamos la extencion a png, lo abrimos y ahi se nos muestra la bandera
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ file flag.txt       
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ mv flag.txt flag.png
                                                                                                                                      
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ open flag.png 
                                                                                                                                      
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ 
picoCTF{now_you_know_about_extensions}
```
## Notas adicionales
## Referencias
