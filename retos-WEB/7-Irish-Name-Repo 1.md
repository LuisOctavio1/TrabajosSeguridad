## Objetivo
Obtener la bandera intentando logearnos como admin

## Solución
```
Aqui entramos en lo que son las inyecciones sql, las cuales son una vulnerabilidad que se pueden dar si se ahcen cosas como concatenar los datos que esta dando el usuario directamente a la sentencia sql, haciendo que este pueda escribir algo que cause un acceso, como por ejemeplo ' or 1==1;, esto hace que el query sea validar la contraseña o que 1 sea igual a 1 haciendo que la sentencia sea verdad siempre y nos de acceso.
la bandera es:picoCTF{s0m3_SQL_f8adf3fb}
```
## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=0EDbUSDqrng&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=7&t=5s
