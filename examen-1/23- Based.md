## Objetivo
Obtener la bandera decifrando los codigos cifrados que te dan a texto

## Solución
```
octa143-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 29221
Let us see how data is stored
submarine
Please give the 01110011 01110101 01100010 01101101 01100001 01110010 01101001 01101110 01100101 as a word.
...
you have 45 seconds.....

Input:
submarine 
Please give me the  143 150 141 151 162 as a word.
Input:
óº
WRONG!
^C
octa143-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 29221
Let us see how data is stored
nurse
Please give the 01101110 01110101 01110010 01110011 01100101 as a word.
...
you have 45 seconds.....

Input:
nurse
Please give me the  164 145 163 164 as a word.
Input:
test
Please give me the 6f76656e as a word.
Input:
oven
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_00a975ff}
```
## Notas adicionales
Se decifra de binario, decimal y hexadecimal
## Referencias
https://gchq.github.io/CyberChef/#input=MTQzIDE1MCAxNDEgMTUxIDE2Mg