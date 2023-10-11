## Objetivo
Intentar acceder a una pagina igual que en el reto pasado
## Solución
```
Aqui seguimos con injecciones sql, pero ahora han agregado un filtro para inyecciones sql, haciendo que la inyeccion pasada no funcione, posiblemente por la palabra or, o el 1, aqui lo que hacemos ahora es hacer con una inyeccion sql hacer que ignore la parte del password, esto lo logramos poniendo al final del usuario ';, esto haciendo que sql ignore todo lo demas de la consulta para darnos el acceso
```
## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=1o53Bwty1E4&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=8
