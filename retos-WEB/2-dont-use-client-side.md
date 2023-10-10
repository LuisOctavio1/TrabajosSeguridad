## Objetivo
Encontrar la bandera que se analiza del lado del cliente

## Solución
```
  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'a3c8') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_1') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '9}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
    
  }
  pico
lo mismo que el pasado, solo tienes que darle a inbspeccionar y se ve que la contraseña se verifica del lado del cliente y no del servidor,ademas, se tiene que ver que la verificacion no esta en orden, asi que tenemos que ver primero el orden que tiene, esto viendo la parte de 0,split, que seria la primera, despues slipt split2, split2 split3 y asi sucecivamente, asi que la contraseña seria 
picoCTF{no_clients_plz_1a3c89}
```
## Notas adicionales
## Referencias
