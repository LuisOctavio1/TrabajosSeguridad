## Objetivo
Obtener la bandera mediante cookies

## Solución
```
Una de las soluciones es desde consola pedir las cookies, automatizandolo para que analice todas las cookies que podamos y asi encontrar la bandera, la linea de comando seria
┌──(kali㉿kali)-[~]
└─$ for i in {0..20}; do curl -s http://mercury.picoctf.net:64944/check -H "Cookie: name=$i"; done | grep picoCTF
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_cc9110ba}</code></p>
y ahi mismo con el grep hacemos que nos de la parte que contenga la bandera
```
## Notas adicionales
## Referencias
https://www.youtube.com/watch?v=LseQ-XWCXVo&list=PLDo9DMLZyP6kTZ8Td37-LdbAx4-yNfHBl&index=12