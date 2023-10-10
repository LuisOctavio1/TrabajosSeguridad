## Objetivo
Encontrar la bandera que esta del lado del cliente

## Solución
```
Es muy parecido al primero, solo que ahora la parte de javaScrip no esta legible esto es porque esta en forma obfuscation, utilizamos una pagina para convertirlo en codigo legible y ahora vemos que la contraseña esta en un array con otros datos basura, el cual es este 
var _0x5a46 = ["37115}", "_again_3", "this", "Password Verified", "Incorrect password", "getElementById", "value", "substring", "picoCTF{", "not_this"];, por logica sabemos que la primera parte es la de pico y podemos descartar algunos como balue, substring stc porque son etiquetas de html, asi que siguiendo esa logica la bandera es picoCTF{not_this_again_337115}
```
## Notas adicionales
## Referencias
http://jsnice.org/
https://www.youtube.com/watch?v=rsPT722MkzQ&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=6