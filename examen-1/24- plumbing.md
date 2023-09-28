## Objetivo
Encontrar la bandera entrando en un servidor que te da mucho texto

## Solución
```
octa143-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 7480 | grep pico
picoCTF{digital_plumb3r_06e9d954}
```
## Notas adicionales
Se hace un pipe con grep para que solo nos de la linea que contenga la bandera.
## Referencias