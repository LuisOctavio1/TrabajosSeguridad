## Objetivo
Encontrar la bandera en un archivo png

## Solución
```
Aqui se nos da un archivo que es una imagen, la cual tenemos que examinar desde un hetidor hexadecimal, con este buscamos la palabra pico para obtener la bandera
File: garden.jpg                                                                        ASCII Offset: 0x0023056E / 0x00230597 (%100)  
00230560  72 65 20 69  73 20 61 20   66 6C 61 67  20 22 70 69                                                         re is a flag "pi
00230570  63 6F 43 54  46 7B 6D 6F   72 65 5F 74  68 61 6E 5F                                                         coCTF{more_than_
00230580  6D 33 33 74  73 5F 74 68   65 5F 33 79  33 36 35 37                                                         m33ts_the_3y3657
00230590  42 61 42 32  43 7D 22 0A                                                                                    BaB2C}".        
                                        
picoCTF{more_than_m33ts_the_3y3657BaB2C}
```
## Notas adicionales
https://www.youtube.com/watch?v=xxhnGxgOtWs&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=14
## Referencias
