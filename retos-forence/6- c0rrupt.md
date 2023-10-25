## Objetivo
Obtener la bandera de un archivo corrompido

## Solución
```
En este reto se nos introduce a lo que son los chuncks de los archivos, los cuales son una serie de bites que identifican el tipo de archivo, los cuales deben tener un formato especifico y nuestra imagen los tiene erroneos, asi que usamos un editor para cambiarlos a mano para que la imagen funcione, a pesar de esto, con el programa pngcheck sigue indicandonos un error, esto porque hay varios errores mas que hacen que no se pueda reconocer el archivo, como que no tiene el IHDR, un error en el chunck pHYs
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ hexeditor mystery
                                                                                                                                      
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ pngcheck -v mystery
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
:  invalid chunk length (too large)
ERRORS DETECTED in mystery
                                                                                                                                      
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ hexeditor mystery  
                                                                                                                                      
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ pngcheck -v mystery
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
:  invalid chunk length (too large)
ERRORS DETECTED in mystery
                                                                                                                                      
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ hexeditor mystery  
                                                                                                                                      
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ pngcheck -v mystery
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
  chunk IDAT at offset 0x00057, length 65445
    zlib: deflated, 32K window, fast compression
  chunk IDAT at offset 0x10008, length 65524
  chunk IDAT at offset 0x20008, length 65524
  chunk IDAT at offset 0x30008, length 6304
  chunk IEND at offset 0x318b4, length 0
No errors detected in mystery (9 chunks, 96.3% compression).
                                                                                                                                      
┌──(kali㉿kali)-[~/escuela/archivosForence]
└─$ open mystery  
esto es la parte final de los comandos que se hicieron para arreglar la imagen, la bandera resulto 
picoCTF{c0rrupt10n_1847995}
```
## Notas adicionales

## Referencias
https://www.youtube.com/watch?v=7zY4VkiWbBI&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=21
