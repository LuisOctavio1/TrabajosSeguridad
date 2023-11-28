## Objetivo

## Solución
```
Parecido al anterior, aqui como el codigo es mas complejo para no calcular
nosotros se pueden hacer break points con el programa y ejecutarlo, para asi
luego inspeccionar los valores y obtener el de eax
(gdb) break main
Breakpoint 1 at 0x40110e
(gdb) run
Starting program: /home/kali/escuela/archivosreverse/debugger0_b 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000000000040110e in main ()
(gdb) break *0x401142
Breakpoint 2 at 0x401142
(gdb) c
Continuing.

Breakpoint 2, 0x0000000000401142 in main ()
(gdb) info registers rip
rip            0x401142            0x401142 <main+60>
(gdb) print/d $eax
$1 = 307019
la bandera quedand
picoCTF{307019}
```
## Notas adicionales
## Referencias