## Objetivo
Obtener la bandera de un programa level2 que nos pedira una contraseña.

## Solución
```
octa143-picoctf@webshell:~$ cat level2.py
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level2.flag.txt.enc', 'rb').read()



def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()
octa143-picoctf@webshell:~$ touch contra.py
octa143-picoctf@webshell:~$ nano contra.py
octa143-picoctf@webshell:~$ python contra.py
4ec9
octa143-picoctf@webshell:~$ python level2.py
Please enter correct password for flag: 4ec9
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_9701e681}
```
## Notas adicionales
Es lo mismo que el problema pasado, solo que ahora se nos pone en codigo ascii, lo que hago es crear un programa de python con el siguiente codigo print (chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)), que da la contraseña para obtener la bandera
## Referencias
