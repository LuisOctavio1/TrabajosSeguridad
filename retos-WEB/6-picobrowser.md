## Objetivo
Encontrar la bandera la cual se da a picobrowser
## Solución
```
Aqui hacemos uso de una parte un header llamado User-Agent, el cual es para identificar el navegador cliente, este header lo podemos modificar desde el el inspeccionar de firefox, analizando el header mandado hacia la consola, dando click en un boton + donde podemos modificar el header y mandarlo, buscamos la parte que dice User-Agent y ahi reemplazamos la parte que dice mozila... por pico browser, lo enviomos y revisamos el get que nos da, donde si vamos a la pestaña de response se podra ver la bandera, la cual es `picoCTF{p1c0_s3cr3t_ag3nt_e9b160d0}`
```
## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=9d6-N0oJwOk&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=5