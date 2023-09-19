# Level 16
## Objetivo
Encontrar un puerto abierto entre 31000 y 32000 que sea ssh y que al darle la contraseña actual nos devuelva las credenciales de el siguiente nivel
## Datos de acceso al nivel
## Solución
```
bandit16@bandit:~$ nmap localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2023-09-19 03:47 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00014s latency).
Not shown: 993 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
1111/tcp  open  lmsocialserver
1840/tcp  open  netopia-vo2
4321/tcp  open  rwhois
8000/tcp  open  http-alt
12345/tcp open  netbus
30000/tcp open  ndmps

Nmap done: 1 IP address (1 host up) scanned in 0.13 seconds
bandit16@bandit:~$ nmap localhost -p 31000-32000
Starting Nmap 7.80 ( https://nmap.org ) at 2023-09-19 03:49 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00010s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds
bandit16@bandit:~$ nmap localhost -p 31000-32000 -sV
Starting Nmap 7.80 ( https://nmap.org ) at 2023-09-19 03:50 UTC
Stats: 0:00:16 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done

bandit16@bandit:~$ openssl s_client -connect  localhost:31046
CONNECTED(00000003)
80DBF0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ openssl s_client -connect  localhost:31518
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Sep 18 14:32:48 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Sep 18 14:32:48 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Sep 18 14:31:48 2023 GMT; NotAfter: Sep 18 14:32:48 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEUcT3EzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwOTE4MTQzMTQ4WhcNMjMwOTE4MTQzMjQ4WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDA
z+VfwT9coRkZdliq3/yoSyGJAcYsnrGgQZCvWplKEEAoXVUo0zuwbywC8ymeMC5T
0Bn+bN46f7Nge2krqA/sqm416pgfq6JZm9XsOa25ZVawoqu3G8Wv6LfY5s7E3Mzu
/syOjyQqCOYFYni9JNqv9K3+gg4qv0DKaj+y6W5KgP2QBCO1XZ5V5TG20gq9Km4f
a3x1K5RjAYEteSF/wsdvWi7QSqskUfi7NLXkob+dloau2yGhAqfOqqPThcm6ZCsV
3hskdmLkt+QpPtdK/slhVzPxEqKGc3jCfzYMhZYZsdCBXZGZ5XK48fr0TFlW6Dga
cfpKvCJtjnFp/XeJTUQNAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQC5
NGdhBRTSAqfKllsfy39l00oJU1iqOsU3HwtudYxmk4t3wSiQNTou1p62i4r9sJSk
5p25YwB5gWRW3AZkXwpkFk3lb524xNJYlV163UAjqfvoapO9opMASalC12azA+Ty
rDrKHynQr8HIwBlH40DtF+0MhMuyRumPFKMsDJhbKYkBnpT+tjNBEjWpuDgdBvmh
0GdkOqT8/nm7wUyJ5/LeucUgrjcjZU3mBVoQHeykRzw0AkJjfaAXKi8eUgHqTBCK
x/xtStXzRu/k/YnwJbK6ynGKACbYS5Alz4Ta3klTiHsm4dIZUFAqbj4KaU2EahAq
h50IKl2+Fsah8/IRwWlb
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
    Session-ID: 2E5527E89634C7453223C53EB661F8FC7A35E16DC7792D7BC38AF4166CA38B1F
    Session-ID-ctx:
    Resumption PSK: 351089B12560D67A97953849C2A85390D37D686421D049DC97497775DB826232381CA1FFCDE900E66332C32B69B5CB83
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 1c 12 9c a5 e3 b5 e2 c4-a5 dd fa a1 99 b4 ac 8e   ................
    0010 - 2a 51 45 66 1d ad 29 b1-4f fe 10 20 38 78 b9 7a   *QEf..).O.. 8x.z
    0020 - 7d 9f 23 ee 84 e2 ff bd-39 30 61 a5 64 c4 33 e9   }.#.....90a.d.3.
    0030 - 8d 95 1a cd d5 a4 6a 18-68 67 9b fb a6 b4 99 2d   ......j.hg.....-
    0040 - a3 1e 6d 83 02 26 5f 2b-e7 cd b4 f6 9c e0 fc ee   ..m..&_+........
    0050 - 21 43 89 95 6d a1 7c 32-a8 ad 7f d9 0b a0 57 16   !C..m.|2......W.
    0060 - 35 a9 df f3 b5 59 6b e0-8c 79 2c b2 9a 79 7e 1f   5....Yk..y,..y~.
    0070 - 65 b4 81 64 59 4f 54 5f-17 5d 48 74 4f 40 eb b8   e..dYOT_.]HtO@..
    0080 - 9f a1 ed ac f9 11 9f da-a6 20 e2 7b 3c 21 c5 c3   ......... .{<!..
    0090 - 38 1d e4 b8 59 03 13 da-f5 64 2c f3 fd 1c 1d bf   8...Y....d,.....
    00a0 - 3d e0 a2 11 e7 47 11 05-45 bb d1 f9 72 dd 72 6a   =....G..E...r.rj
    00b0 - 13 34 d0 48 4f 1e 46 6b-93 ff d9 40 c3 a2 c0 76   .4.HO.Fk...@...v
    00c0 - a9 46 b5 e7 3e 0a 36 42-fa 2c a7 35 54 4f e9 c5   .F..>.6B.,.5TO..

    Start Time: 1695095485
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
    Session-ID: 857F50517A687B5DF086DAEE39C06F3173B3D510EB8A41BD619AB10E2C4C2D4E
    Session-ID-ctx:
    Resumption PSK: 9B66C34453BF730BA247CF4A98B5DC068BAA9278952B09DCBDD528D870199F3543B8BD2F1F7CA62837BFC203D274B308
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 1c 12 9c a5 e3 b5 e2 c4-a5 dd fa a1 99 b4 ac 8e   ................
    0010 - a0 63 39 a1 99 51 6c ee-c0 65 0d e8 5e 34 37 5b   .c9..Ql..e..^47[
    0020 - 4f 8a b2 12 1d b1 78 0e-5b 64 6a 83 18 0c 9b 43   O.....x.[dj....C
    0030 - 00 ef 55 fe f4 aa e9 0c-96 57 47 f3 a9 8b d1 88   ..U......WG.....
    0040 - b1 fa 19 0f e5 06 03 06-e5 0e 56 a3 68 9b c7 13   ..........V.h...
    0050 - 41 59 fe b1 64 3e ff 0e-86 47 25 cb 46 6d a9 ce   AY..d>...G%.Fm..
    0060 - a5 fd 2b e7 99 d1 3a c6-ba 47 5b c0 fa 2d 6e 85   ..+...:..G[..-n.
    0070 - ae ee 5c 28 6c 8b 03 9b-9f 55 03 20 55 6c 28 1b   ..\(l....U. Ul(.
    0080 - dc f2 70 45 2f e8 ae c8-a7 ee 1d 0d d8 e1 77 f3   ..pE/.........w.
    0090 - 7e 41 d4 69 68 44 b7 29-88 f8 ad 51 80 93 a8 7f   ~A.ihD.)...Q....
    00a0 - 88 f1 b9 94 ce 4b a2 41-d9 f4 85 f4 a7 5c ba 99   .....K.A.....\..
    00b0 - 37 76 7e 44 2a 0a 43 b0-a5 fb 9d d0 dd ff a0 41   7v~D*.C........A
    00c0 - fb 3c ec 48 ad 72 79 5d-9b 30 34 76 c3 0f 88 08   .<.H.ry].04v....

    Start Time: 1695095485
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
JQttfApK4SeyHwDlI9SXGR50qclOAil1
JQttfApK4SeyHwDlI9SXGR50qclOAil1
exit
exit
^C
bandit16@bandit:~$ openssl s_client -connect  localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Sep 18 14:32:48 2023 GMT
verify return:1
depth=0 CN = localhost
notAfter=Sep 18 14:32:48 2023 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Sep 18 14:31:48 2023 GMT; NotAfter: Sep 18 14:32:48 2023 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEb7jfsDANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjMwOTE4MTQzMTQ4WhcNMjMwOTE4MTQzMjQ4WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDF
/JRVSGUn03lXEGF3AegYY+mPc6ZozCOGy7hYlVO0DfAtuMj3QiiwF7K3NKscjQSU
yPtOA4mfOC+QAmLSC/Kwi7GjAiPKD8u7NgjNES92o2tsfy/UKtDhYxazMFycbesh
eUvZStB7rEpWY3p4AAbVpSGnbiuriTBVNmrKqAz0dDYDFVWsS/K6isQeuahqJ/Nr
LW2WvucEHyvE49dcfc9FiQOqyeV17diRuZhV9cJGh5ld0uEHftocjFLRIWgDuLGn
EMJYPlPxmQi1aDnUU6mvtlUCFAqrMUK+svaaEMuOF6ljrgHb0NVJ7QlVwM6JCLpi
/F6eg2hLENneSkKVkwhfAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQCW
cS0a0udS+PuAsBPaDO9li2pcRiiWmMFtZMjskpk7ggmu+dWwy1Hyhe15mwhtRMHc
mSIDcmpnsQhXnNdygPkASDYuBMvEF3x2lrtevEc/tsgWI0jiu4GHY9/xgV1yi0g/
/cj9uEeYZu9f742QV0XVfcVIljCSvT3Ic47MerUKttZ19RVpALuGaWk8++a535x9
gOtfFUs1LGXuphHVvB1Kdj5icD74PV1ZFXV6e7TheMUgrMjJb93T3cyM8IWIuEGu
Z/garZZVV4DetxbSioTgZx7FPdnQ+xg7/gMqsSeoV1ouTN5gEkOmva+qkk2+C+FC
jNEIr/7SZciUS0Nimpcm
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
    Session-ID: 59F7071B3F8957FE387AAC9A9B8A4C716F4A11CE608C43A48A30251C7C25D615
    Session-ID-ctx:
    Resumption PSK: DBB5C34F938766E5595E2D4BE09F9D96D5C34B534C0DFC99E65E6E31E3F31A0FC3EF719DA0DC9C01BC44B22C21912194
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - f1 d7 8c 2f 7c 5d 01 37-ac 93 cd d3 c4 31 18 b8   .../|].7.....1..
    0010 - 44 90 8e a5 de 9c ac 58-0f d7 e4 e6 83 d8 34 7a   D......X......4z
    0020 - e0 c9 5b c3 a4 2b dd 91-3b 8f 2e c1 f8 40 f8 81   ..[..+..;....@..
    0030 - b4 5e 3d dc 5b d4 8a a3-35 fe 36 2b 77 1e aa 61   .^=.[...5.6+w..a
    0040 - c0 b2 3d fe fa f0 23 fa-43 d1 c0 0d fc c6 71 77   ..=...#.C.....qw
    0050 - 9e 62 5a d6 40 e3 40 d4-81 04 f5 a5 61 86 44 aa   .bZ.@.@.....a.D.
    0060 - b7 ef 42 48 39 f2 d5 9d-85 51 37 e0 c3 a8 e8 ee   ..BH9....Q7.....
    0070 - 26 b1 8c 28 86 ec e2 26-ea f6 f6 5e ec 42 2f ae   &..(...&...^.B/.
    0080 - 9a 6e 51 17 20 94 a7 1c-9c cc 90 f3 b8 d5 42 a4   .nQ. .........B.
    0090 - 06 83 15 cf 56 bc 03 4e-24 fb 96 ef ea b2 6e 97   ....V..N$.....n.
    00a0 - 79 08 d8 96 58 1b bb 10-0f 7e b8 66 ce cf 57 9c   y...X....~.f..W.
    00b0 - af 71 49 1c 16 99 47 75-b1 bb f2 a6 7a 28 08 ee   .qI...Gu....z(..
    00c0 - e5 a8 ea ff 49 7b a1 ef-c7 6d 7f 7f 19 69 ed 2f   ....I{...m...i./

    Start Time: 1695095520
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
    Session-ID: AB2F181CE836339AFCAE3F678E53E4E2F101D9A6FD5CAB0CBB4708657B19F4C9
    Session-ID-ctx:
    Resumption PSK: 034A662352F6C9A5A336D894FC2AC5AA7F94A4B072D79439220786CD8949B00B39E4F82390AB1E83FADC0CA1AB9B3EC2
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - f1 d7 8c 2f 7c 5d 01 37-ac 93 cd d3 c4 31 18 b8   .../|].7.....1..
    0010 - ec 62 36 d1 77 be a8 fa-ff bf ca d5 2e d5 bf cc   .b6.w...........
    0020 - c4 d5 be d1 17 71 ee d1-f2 aa 29 3d 83 8a 8b 6e   .....q....)=...n
    0030 - 04 dc bf d4 cd 68 9e 9c-2c 47 e0 72 4c 5e a7 ad   .....h..,G.rL^..
    0040 - 78 72 15 e9 0e 92 9d 56-25 8a ea da 45 70 f8 b8   xr.....V%...Ep..
    0050 - ec 69 42 a0 43 fc 63 01-9a 44 4d f4 66 eb 7c be   .iB.C.c..DM.f.|.
    0060 - 70 1b cf e5 02 2d d7 c2-2e 5f 0d 8d b8 66 41 c1   p....-..._...fA.
    0070 - 65 df 8e 0c 48 4f 6f 25-99 f3 26 b8 84 4f dd 7a   e...HOo%..&..O.z
    0080 - cf 95 8b a4 47 e2 bd f0-fd b3 b3 8f d3 c7 81 f6   ....G...........
    0090 - de cc 5d f5 03 1b a2 8b-4f 1f 51 42 a4 76 68 fe   ..].....O.QB.vh.
    00a0 - ea 0b 2c 3f 44 8b 0d 8e-eb 37 29 53 30 fd c4 b9   ..,?D....7)S0...
    00b0 - dd 63 98 5f 34 2f df 51-fe d6 6b c7 03 47 61 0a   .c._4/.Q..k..Ga.
    00c0 - 9c 4c 96 3a 3d 2c 9a 64-f6 be 2c e1 53 27 bb 43   .L.:=,.d..,.S'.C

    Start Time: 1695095520
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
JQttfApK4SeyHwDlI9SXGR50qclOAil1
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
bandit16@bandit:~$ exit
```
## Notas adicionales
Lo primero que hacemos es utilizar nmap para ver que puertos están abiertos entre el puerto 31000 y 32000, esto con el parámetro -p, dándonos varios, luego nos intentamos conectar a cada uno vía ssh hasta que sea el que nos de la contraseña, en este caso una llave ssh.
## Referencias
