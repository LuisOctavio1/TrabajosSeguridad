## Objetivo

## Solución
```
Se dan los valores de c,n y e, y se puede ver que el valor de n es pequeño,
con lo cual se podria factorizar para obtener q y p, se realiza con una
herramienta externa y onbtenemos p y q, y ahora solo es hacer las operaciones
con la formula
from Crypto.Util.number import inverse

from Crypto.Util.number import long_to_bytes

p = 1461849912200000206276283741896701133693

q =  431899300006243611356963607089521499045809

c= 421345306292040663864066688931456845278496274597031632020995583473619804626233684

n= 631371953793368771804570727896887140714495090919073481680274581226742748040342637

e= 65537

  

tn = (p-1)*(q-1)

d = inverse(e,tn)

desencriptado = pow(c,d,n)

  

print(long_to_bytes(desencriptado))
```
## Notas adicionales
## Referencias