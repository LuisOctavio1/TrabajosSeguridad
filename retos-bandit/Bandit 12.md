# Level 12
## Objetivo
Obtener la contraseña, la cual fue empaquetada múltiples veces
## Datos de acceso al nivel
**bandit12@bandit.labs.overthewire.org**
JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
## Solución
```
ls  
data.txt  
bandit12@bandit:~$ mkdir /tmp/luisOctavio  
bandit12@bandit:~$ cat data.txt | xxd -r > /tmp/luisOctavio  
-bash: /tmp/luisOctavio: Is a directory  
bandit12@bandit:~$ cat data.txt | xxd -r > /tmp/luisOctavio/datos  
bandit12@bandit:~$ cd tmp/luisOctavio  
-bash: cd: tmp/luisOctavio: No such file or directory  
bandit12@bandit:~$ cd /tmp/luisOctavio  
bandit12@bandit:/tmp/luisOctavio$ ls  
datos  
bandit12@bandit:/tmp/luisOctavio$ cat datos  
bandit12@bandit:/tmp/luisOctavio$ file datos  
datos: gzip compressed data, was "data2.bin", last modified: Sun Apr 23   18:04:23 2023, max compression, from Unix, original size modulo 2^32 581  
bandit12@bandit:/tmp/luisOctavio$ mv datos datos.gz  
bandit12@bandit:/tmp/luisOctavio$ ls  
datos.gz  
bandit12@bandit:/tmp/luisOctavio$ file datos.gz  
datos.gz: gzip compressed data, was "data2.bin", last modified: Sun Apr 23   18:04:23 2023, max compression, from Unix, original size modulo 2^32 581  
bandit12@bandit:/tmp/luisOctavio$ gzip -d datos.gz  
gzip: datos already exists; do you wish to overwrite (y or n)? y  
bandit12@bandit:/tmp/luisOctavio$ file datos  
datos: bzip2 compressed data, block size = 900k  
bandit12@bandit:/tmp/luisOctavio$ mc datos datos.bz2  
Command 'mc' not found, but can be installed with:  
apt install mc  
Please ask your administrator.  
bandit12@bandit:/tmp/luisOctavio$ ls  
datos  
bandit12@bandit:/tmp/luisOctavio$ mv datos datos.bz2   
bandit12@bandit:/tmp/luisOctavio$ ls  
datos.bz2  
bandit12@bandit:/tmp/luisOctavio$ bzip2 -d datos.bz2  
bandit12@bandit:/tmp/luisOctavio$ ls  
datos  
bandit12@bandit:/tmp/luisOctavio$ file datos  
datos: gzip compressed data, was "data4.bin", last modified: Sun Apr 23   18:04:23 2023, max compression, from Unix, original size modulo 2^32 20480  
bandit12@bandit:/tmp/luisOctavio$ mv datos datos.gz  
bandit12@bandit:/tmp/luisOctavio$ gzip -d datos.gz  
bandit12@bandit:/tmp/luisOctavio$ ls  
datos  
bandit12@bandit:/tmp/luisOctavio$ file datos  
datos: POSIX tar archive (GNU)  
bandit12@bandit:/tmp/luisOctavio$ mv datos datos.tar  
bandit12@bandit:/tmp/luisOctavio$ ls  
datos.tar  
bandit12@bandit:/tmp/luisOctavio$ tar xf datos.tar  
bandit12@bandit:/tmp/luisOctavio$ ls  
data5.bin  datos.tar  
bandit12@bandit:/tmp/luisOctavio$ rm datos.tar  
bandit12@bandit:/tmp/luisOctavio$ ls  
data5.bin  
bandit12@bandit:/tmp/luisOctavio$ file data5.bin  
data5.bin: POSIX tar archive (GNU)  
bandit12@bandit:/tmp/luisOctavio$ mv data5.bin data5.tar  
bandit12@bandit:/tmp/luisOctavio$ ls  
data5.tar  
bandit12@bandit:/tmp/luisOctavio$ tar xf data5.tar  
bandit12@bandit:/tmp/luisOctavio$ ls  
data5.tar  data6.bin  
bandit12@bandit:/tmp/luisOctavio$ rm data5.tar  
bandit12@bandit:/tmp/luisOctavio$ file data6.bin  
data6.bin: bzip2 compressed data, block size = 900k  
bandit12@bandit:/tmp/luisOctavio$ mv data6.bin data6.bz2  
bandit12@bandit:/tmp/luisOctavio$ ls  
data6.bz2  
bandit12@bandit:/tmp/luisOctavio$ bzip2 -d data6.bz2  
bandit12@bandit:/tmp/luisOctavio$ ls  
data6  
bandit12@bandit:/tmp/luisOctavio$ file data6  
data6: POSIX tar archive (GNU)  
bandit12@bandit:/tmp/luisOctavio$ mv data6 data6.tar  
bandit12@bandit:/tmp/luisOctavio$ ls  
data6.tar  
bandit12@bandit:/tmp/luisOctavio$ tar xf data6.tar  
bandit12@bandit:/tmp/luisOctavio$ ls  
data6.tar  data8.bin  
bandit12@bandit:/tmp/luisOctavio$ rm data6.tar  
bandit12@bandit:/tmp/luisOctavio$ file data8  
data8: cannot open `data8' (No such file or directory)  
bandit12@bandit:/tmp/luisOctavio$ file data8.bin  
data8.bin: gzip compressed data, was "data9.bin", last modified: Sun Apr 23  18:04:23 2023, max compression, from Unix, original size modulo 2^32 49  
bandit12@bandit:/tmp/luisOctavio$ mv data8.bin  data8.gz  
bandit12@bandit:/tmp/luisOctavio$ ls  
data8.gz  
bandit12@bandit:/tmp/luisOctavio$ gzip -d data8.gz  
bandit12@bandit:/tmp/luisOctavio$ ls  
data8  
bandit12@bandit:/tmp/luisOctavio$ cat data8  
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw  
```
## Notas adicionales
Lo primero que se hace es hacer un directorio para poder crear y modificar archivos, revisamos de que tipo es el archivo para saber con que comando descomprimir y así sucesivamente hasta que se obtiene un txt con la contraseña
## Referencias
