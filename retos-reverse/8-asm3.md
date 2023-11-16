## Objetivo

## Solución
```
En este reto ahora hay partes de que estan en 16 y 8 bits, cosa que podria
ser algo tardado, por lo que se utilizara un emulador, hacemos algunas
modificaciones al codigo y asi que:
start:
	push 0xe54409d5
	push 0xe6cf51f0
	push 0xd2c26416
	call asm3

asm3:
		push   ebp
		mov    ebp,esp
		xor    eax,eax
		mov    ah,BYTE PTR [ebp+0x9]
		shl    ax,0x10
		sub    al,BYTE PTR [ebp+0xe]
		add    ah,BYTE PTR [ebp+0xf]
		xor    ax,WORD PTR [ebp+0x12]
		nop
		pop    ebp
		ret 
y la bandera es 0x375
```
## Notas adicionales
## Referencias
