datos = open('message.txt').read().split()
bandera = ""
for i in datos:
    modu = int(i) % 37
    if modu >= 0 and modu <=25:
        bandera += chr(modu+65)
    elif modu >=26 and modu<=35:
        bandera += chr(modu+22)
    else:
        bandera+= '_'

print("picoCTF{" + bandera + "}")