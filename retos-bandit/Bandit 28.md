
# Level 28
## Objetivo
Encontrar la credencial en un repositorio de git
## Datos de acceso al nivel
AVanL161y9rsbcJIsFHuw35rjaOM19nR
## Solución
```
bandit28@bandit:/tmp/tmp.UmO5Iq1G3X$ ls
repo
bandit28@bandit:/tmp/tmp.UmO5Iq1G3X$ cd repo/
bandit28@bandit:/tmp/tmp.UmO5Iq1G3X/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.UmO5Iq1G3X/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.UmO5Iq1G3X/repo$ ls -la
total 16
drwxrwxr-x 3 bandit28 bandit28 4096 Oct  3 01:47 .
drwx------ 3 bandit28 bandit28 4096 Oct  3 01:47 ..
drwxrwxr-x 8 bandit28 bandit28 4096 Oct  3 01:47 .git
-rw-rw-r-- 1 bandit28 bandit28  111 Oct  3 01:47 README.md
bandit28@bandit:/tmp/tmp.UmO5Iq1G3X/repo$ git log
commit 899ba88df296331cc01f30d022c006775d467f28 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Sun Apr 23 18:04:39 2023 +0000

    fix info leak

commit abcff758fa6343a0d002a1c0add1ad8c71b88534
Author: Morla Porla <morla@overthewire.org>
Date:   Sun Apr 23 18:04:39 2023 +0000

    add missing data

commit c0a8c3cf093fba65f4ee0e1fe2a530b799508c78
Author: Ben Dover <noone@overthewire.org>
Date:   Sun Apr 23 18:04:39 2023 +0000

    initial commit of README.md
bandit28@bandit:/tmp/tmp.UmO5Iq1G3X/repo$ git checkout 899ba88df296331cc01f30d022c006775d467f28
Note: switching to '899ba88df296331cc01f30d022c006775d467f28'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 899ba88 fix info leak
bandit28@bandit:/tmp/tmp.UmO5Iq1G3X/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/tmp.UmO5Iq1G3X/repo$ git checkout abcff758fa6343a0d002a1c0add1ad8c71b88534
Previous HEAD position was 899ba88 fix info leak
HEAD is now at abcff75 add missing data
bandit28@bandit:/tmp/tmp.UmO5Iq1G3X/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S
```
## Notas adicionales
Basicamente lo que se hace aqui es lo mismo que en el reto 27, pero al dar cat a el archivo readme sale oculta la contraseña, viendo el log de git se puede ver como hay un commit que se llama arreglando el leak, hacemos un git checkout a ese commit y al dar cat al archivo ahora si se ve la contraseña
## Referencias
