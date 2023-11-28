from pwn import *
import primefac
from itertools import combinations
from Crypto.Util.number import long_to_bytes

def sub_lists (l):
    comb = []
    for i in range(1,len(l)+1):
        comb += [list(j) for j in combinations(l, i)]
    return comb

def divisors(phi):
   print("Give me the divisors of ", phi-1)
   return(eval(input()))

#conectando al servidor
r = remote('saturn.picoctf.net', 58675)
r.recvuntil("anger =")
ciphertext=int(r.recvline())
r.recvuntil("envy =")
d=int(r.recvline())
print("cipher=",ciphertext)
print("d=",d)
print(r.recvuntil("vainglory?"))
r.recvline()
factores=divisors(d*65537)
combos = sub_lists(factores)
primos = set()
for l in combos:
   producto = 1
   for k in l:
      producto = producto * k
   if producto.bit_length()==128 and primefac.isprime(producto+1):
      primos.add(producto+1)
print(primos)
listaPrimos = list(primos)
#se tratan todas los posibles numeros primos
for p in listaPrimos:
   for q in listaPrimos:
      n=p*q
      plain = pow(ciphertext,d,n)
      try:
         plaintext = long_to_bytes(plain)
         print(plaintext.decode())
         r.sendline(plaintext.decode())
         print(r.recvline())
         print(r.recvline())
         print(r.recvline())
      except:
         continue
