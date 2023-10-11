## Objetivo
Continuacion de los pasados 3

## Solución
```
Aqui es igual con sql injection, utilizando el campo debugger se puede notar que la contraseña que eviamos esta encriptada, esto en rot13, que es una encriptaccion insegura porque es muy facil de notar, asi qe al poner ' or 1=1; se nos cambia a ' be 1=1;, asi que si ponemos ahora eso de contraseña sa cambia a ' or 1=1; y nos da acceso, la contraseña es picoCTF{3v3n_m0r3_SQL_7f5767f6}
```
## Notas adicionales
## Referencias
