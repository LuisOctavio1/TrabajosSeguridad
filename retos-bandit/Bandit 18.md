# Level 18
## Objetivo
Obtener la contraseña de un archivo readme en el servidor que en cuanto entramos automáticamente nos saca.
## Datos de acceso al nivel
bandit18@bandit.labs.overthewire.org
hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

## Solución
```
PS C:\Users\PC\OneDrive\Escritorio\Escuela\7mo\seguridad\notas\trabajosYnotas> ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
PS C:\Users\PC\OneDrive\Escritorio\Escuela\7mo\seguridad\notas\trabajosYnotas>
```
## Notas adicionales
Lo que hacemos aquí es al final de la conexión es poner el comando cat readme que hace que la primera cosa que se haga sea leer el archivo, se lee y nos saca automáticamente, obteniendo la contraseña.
## Referencias