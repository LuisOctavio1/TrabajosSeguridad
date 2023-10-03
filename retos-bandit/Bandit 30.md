# Level 30
## Objetivo
## Datos de acceso al nivel
xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS
## Solución
```
bandit30@bandit:/tmp/tmp.tV3mckszTf/repo$ git branch -r
  origin/HEAD -> origin/master
  origin/master
bandit30@bandit:/tmp/tmp.tV3mckszTf/repo$ git checkout master
Already on 'master'
Your branch is up to date with 'origin/master'.
bandit30@bandit:/tmp/tmp.tV3mckszTf/repo$ git checkout HEAD
Your branch is up to date with 'origin/master'.
bandit30@bandit:/tmp/tmp.tV3mckszTf/repo$ ls
README.md
bandit30@bandit:/tmp/tmp.tV3mckszTf/repo$ git log
commit 59530d30d299ff2e3e9719c096ebf46a65cc1424 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Sun Apr 23 18:04:42 2023 +0000

    initial commit of README.md
bandit30@bandit:/tmp/tmp.tV3mckszTf/repo$ git tag
secret
bandit30@bandit:/tmp/tmp.tV3mckszTf/repo$ git show secret
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
```
## Notas adicionales
Aqui la contraseña no esta oculta en una rama o comit, si no en un tag, el cual al verlo nos da la contraseña
## Referencias
