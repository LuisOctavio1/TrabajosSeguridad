# Level 29
## Objetivo
Obtener los clonando un repositorio de git
## Datos de acceso al nivel
tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S
## Solución
```
bandit29@bandit:/tmp/tmp.FCzqURJzQU$ ls
repo
bandit29@bandit:/tmp/tmp.FCzqURJzQU$ cd repo/
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git log
commit 4bd5389f9f2b9e96ba517aa751ee58d051905761 (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Sun Apr 23 18:04:40 2023 +0000

    fix username

commit 1a57cf10158f133c4f40ff82251f605a7618631d
Author: Ben Dover <noone@overthewire.org>
Date:   Sun Apr 23 18:04:40 2023 +0000

    initial commit of README.md
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git branch HEAD
fatal: 'HEAD' is not a valid branch name.
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git branchs
git: 'branchs' is not a git command. See 'git --help'.

The most similar command is
        branch
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git branch
* master
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git checkout HEAD
Your branch is up to date with 'origin/master'.
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git checkout 4bd5389f9f2b9e96ba517aa751ee58d051905761
Note: switching to '4bd5389f9f2b9e96ba517aa751ee58d051905761'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 4bd5389 fix username
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ LS
LS: command not found
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git checkout
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git log
commit 4bd5389f9f2b9e96ba517aa751ee58d051905761 (HEAD, origin/master, origin/HEAD, master)
Author: Ben Dover <noone@overthewire.org>
Date:   Sun Apr 23 18:04:40 2023 +0000

    fix username

commit 1a57cf10158f133c4f40ff82251f605a7618631d
Author: Ben Dover <noone@overthewire.org>
Date:   Sun Apr 23 18:04:40 2023 +0000

    initial commit of README.md
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git checkout 1a57cf10158f133c4f40ff82251f605a7618631d
Previous HEAD position was 4bd5389 fix username
HEAD is now at 1a57cf1 initial commit of README.md
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit29
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git branch -r
  origin/HEAD -> origin/master
  origin/dev
  origin/master
  origin/sploits-dev
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ git checkout sploits-dev
Previous HEAD position was 1a57cf1 initial commit of README.md
Branch 'sploits-dev' set up to track remote branch 'sploits-dev' from 'origin'.
Switched to a new branch 'sploits-dev'
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ ls
exploits  README.md
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ cat exploits/
cat: exploits/: Is a directory
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ cd exploits/
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/exploits$ ls
horde5.md
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/exploits$ cat horde5.md

bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/exploits$ git checkout dev
Branch 'dev' set up to track remote branch 'dev' from 'origin'.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/exploits$ ls
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/exploits$ cd ..
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ ls
code  README.md
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ cd code/
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/code$ ls
gif2ascii.py
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/code$ cat gif2ascii.py

bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/code$ python gif2ascii.py
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/code$ python3 gif2ascii.py
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo/code$ cd ..
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ car README.md
Command 'car' not found, but can be installed with:
apt install ucommon-utils
Please ask your administrator.
bandit29@bandit:/tmp/tmp.FCzqURJzQU/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS
```
## Notas adicionales
Lo mismo para clonar el repositorio, ahora en vez de revisar los commits revisamos las ramas que hay, revise una y luego la dev, donde al darle el cat al readme si se muestra la contraseña
## Referencias
