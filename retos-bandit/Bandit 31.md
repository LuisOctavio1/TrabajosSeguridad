# Level X
## Objetivo
## Datos de acceso al nivel
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
## Solución
```
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ cat README.md
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ rm .gitignore
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ ls -la
total 16
drwxrwxr-x 3 bandit31 bandit31 4096 Oct  3 03:36 .
drwx------ 3 bandit31 bandit31 4096 Oct  3 03:33 ..
drwxrwxr-x 8 bandit31 bandit31 4096 Oct  3 03:33 .git
-rw-rw-r-- 1 bandit31 bandit31  147 Oct  3 03:33 README.md
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ nano key.txt
Unable to create directory /home/bandit31/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ touch key.txt
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ nano key.txt
Unable to create directory /home/bandit31/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ ls
key.txt  README.md
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ cat key.txt
May I come in?
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ git add .
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ git commit -am "agregando lo solicitado"
[master e906356] agregando lo solicitado
 2 files changed, 1 insertion(+), 1 deletion(-)
 delete mode 100644 .gitignore
 create mode 100644 key.txt
bandit31@bandit:/tmp/tmp.KIYOZb2Qev/repo$ git push origin master
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Could not create directory '/home/bandit31/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit31-git@localhost's password:
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 295 bytes | 295.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: ### Attempting to validate files... ####
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
remote: Well done! Here is the password for the next level:
remote: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
To ssh://localhost:2220/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://localhost:2220/home/bandit31-git/repo'
```
## Notas adicionales
Aqui al leer el readme se nos pide crear un archivo llamado key.txt que tenga el mesaje puedo entrar?, con touch creamos el archivo y con nano lo modifico, hago al add, comit y push a da la contraseña
## Referencias
