# Level 15
## Objetivo
Dar la contraseña del nivel actual en el puerto 30001 usando SSL
## Datos de acceso al nivel
**bandit15@bandit.labs.overthewire.org**
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
## Solución
```
bandit15@bandit:~$ ls
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Sep 17 08:03:36 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Sep 17 08:03:36 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Sep 17 08:02:36 2023 GMT; NotAfter: Sep 17 08:03:36 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEeW0MujANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwOTE3MDgwMjM2WhcNMjMwOTE3MDgwMzM2WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDE
oRX/H4qjwHCLneK/4xT13Q9kjKLU9+76eFWp5DuqvOU9qDwf6ZRPXyjW1vJ0UrXm
+me1SLmMoRHK+O88QUVxOaDAWePIn2B5QCuCF7gDjbbp51hCgNUvJqb+fn5miibQ
4aZxiBbC3RmpxHL8bzDHRbZtQtENEEbFYkuQP0d1uQjPkwpU3664TW0ssh+aaz8Z
CIKUfVB1IpYCPcAbhKROOpUiaUozW04dgOv0QQfqXB0/3wOe/xW/dhjR1vm5ir1y
CGOPN9n1MmImhFf3cUIRD2wnO6U0SVIUokSOr4Lpwy5j5Zo8u85AxErmQTf4RPsw
yAP0aFprsHvSndaMr+dJAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQCF
GXDOH5ZVmrPsa+5wp/tZQ7tEH9JJ9pVGsBN65YcdbfsjZpW9zhSxJCF8baFmR6ht
1HVJd+jeuNKncs7plLR+7k5wCbzQmwpZquUymKAdSfMFxD5FepKOajSZCe0yu+SK
kcOb4Y/v6lpltmpDI9MGlBW7cY9uy3tLQvoTu2Tq/Y4Kicm+Ass9c5SkhnMMb0wL
q5nNDYfLm6wQesYXw4zOu/QK/A1NTHTGz3uaznytLFmFm3Yv8IVz6C3GDB/DKkAk
cc8Con5QEVy59IC7uosR+6853xpeLomiK/CqgT8gWjVUnw34jEXEO+OPBDVLhMF1
TJk6AxA+iXZOJy1IuThT
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 33D05DEF6D99D314165EC7842525235A2C9DEE22158703443ED3419E4EF09E96
    Session-ID-ctx:
    Resumption PSK: BD1FC2564CFE20B3C1036447237D64E852323F9F91C813F716577828CE324D7CD46D82D9FE8CDDC4D4ACE19D43823AA2
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - fc 4b 37 d8 7a 5e 3f dd-ff 0a 29 a4 85 99 71 54   .K7.z^?...)...qT
    0010 - b0 d8 01 ae 78 d4 80 11-d7 28 19 b5 ed 0f c9 7d   ....x....(.....}
    0020 - ab 69 d0 ed 78 f2 98 d9-60 b2 22 17 c2 00 44 40   .i..x...`."...D@
    0030 - 59 0c 1f 02 08 1a a7 76-b7 5e a5 2f 1d a8 c7 1f   Y......v.^./....
    0040 - ba 95 bc a2 96 3a 9b 6c-05 ef aa 22 31 d2 16 65   .....:.l..."1..e
    0050 - 3a a8 49 ac cb a1 9c 9f-bc e1 70 53 35 69 06 e6   :.I.......pS5i..
    0060 - 47 1c 7e 3b ab e8 04 09-cc eb c7 21 4e d1 9a 0c   G.~;.......!N...
    0070 - c8 55 a3 08 5d e8 3a f8-8c 8a 02 eb 6d 97 b3 bc   .U..].:.....m...
    0080 - 04 a4 73 82 92 b7 a6 68-f4 1d 3b ca 7c 96 ae fe   ..s....h..;.|...
    0090 - 24 90 3a 6d 1f 1c d0 08-bb 8b 2a 8e f6 ef e4 d5   $.:m......*.....
    00a0 - d7 45 11 b5 bb a2 50 6e-7f 84 9a c7 cd 60 6a 8b   .E....Pn.....`j.
    00b0 - de bc df a8 0d d9 c9 cc-54 b2 f0 0e df 34 7a 44   ........T....4zD
    00c0 - 11 a3 06 a4 44 4a d2 b2-5b d4 ac 38 33 9f 4e 55   ....DJ..[..83.NU

    Start Time: 1695013583
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 283AF5AD9FE23ADE190B5981481E900B60913A781D0DD0BAA17FC646E0B48A8B
    Session-ID-ctx:
    Resumption PSK: C7C39A193144F3AC8C60E550AC5F0133F2FB542A66CD84CE714E0305911E9334794C9D458A3826A0A42640A2AD1BFA8D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - fc 4b 37 d8 7a 5e 3f dd-ff 0a 29 a4 85 99 71 54   .K7.z^?...)...qT
    0010 - 2f f5 ab 5e 41 07 6e 20-63 ea 84 b8 52 71 0a ab   /..^A.n c...Rq..
    0020 - 44 62 b3 be ba 15 7a cf-eb b2 5d c0 7e 53 9f 50   Db....z...].~S.P
    0030 - 55 bf d2 4e cc 66 c1 ca-77 32 44 a2 fd 76 d9 ef   U..N.f..w2D..v..
    0040 - 24 f9 dd 74 05 0e 69 db-ea 6c 49 b3 4f d7 18 46   $..t..i..lI.O..F
    0050 - e4 27 5f 95 33 ad 74 cf-8f 2b 9f 61 c2 2c 68 be   .'_.3.t..+.a.,h.
    0060 - 67 58 56 71 15 f2 1e c6-a0 b7 c5 65 ac 26 26 f8   gXVq.......e.&&.
    0070 - 20 a1 35 85 71 6c cd 82-c6 d7 07 8c 1c 66 89 ba    .5.ql.......f..
    0080 - 07 1f 94 d0 8d 64 ee 95-28 86 8f ae 1f 6c 38 15   .....d..(....l8.
    0090 - 99 bf 83 62 9c 14 97 14-82 c4 89 70 2e b7 6b 59   ...b.......p..kY
    00a0 - 82 c1 e5 f4 34 27 52 4d-e7 40 6b 6e 73 f3 39 ec   ....4'RM.@kns.9.
    00b0 - 15 10 73 64 65 cc 87 1c-db 2a 9c dd 45 53 fd 38   ..sde....*..ES.8
    00c0 - 85 f6 4b 87 f4 fb f3 d7-4a ea 52 fe 80 d1 a7 e0   ..K.....J.R.....

    Start Time: 1695013583
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
```
## Notas adicionales
El comando openssl nos ayuda a conectarnos de manera ssl, haciendo que cuando enviemos información este encriptada , esto haciendo que no nos desconecte, dando la contraseña actual y devolviendo la nueva.
## Referencias