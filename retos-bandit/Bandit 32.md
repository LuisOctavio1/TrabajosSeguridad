# Level X
## Objetivo
## Datos de acceso al nivel
rmCBvG56y58BXzv98yZGdO7ATVL5dW8y
## Solución
```
WELCOME TO THE UPPERCASE SHELL
>>
>> ls
sh: 1: LS: Permission denied
>> sh
sh: 1: SH: Permission denied
>>
>> $SH
>> $0
$ export SHELL=/bin/bash
sh: 1: export: SHELL�: bad variable name
$ export SHELL=/bin/bash
$ $SHELL
bandit33@bandit:~$ ls
uppershell
```
## Notas adicionales
Aqui lo que hacemos es jugar con los parametros pocisionales, esto para poder poner el export shell y que podamos acceder a la consola normal, ya no hay mas contraseñas pues es el ultimo reto.
## Referencias
https://bash.cyberciti.biz/guide/How_to_use_positional_parameters