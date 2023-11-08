datos = open('encrypted.txt').read()
bandera = ""
for i in datos:
    if 'a' <= i <= 'z':
        bandera+= chr(122 - (ord(i) - 97))
    elif 'A' <= i <= 'Z':
        bandera+= chr(90 - (ord(i) - 65))
    else:
        bandera+=i

print(bandera)
