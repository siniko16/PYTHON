import random

karakterler = ("1234567890pouytreq1wasdf")

sifre_uzunlugu = int(input("sifrenin uzunlugunu giriniz: "))
sifre = ""

for i in range(sifre_uzunlugu):
    sifre = sifre + random.choice(karakterler)

print(sifre)