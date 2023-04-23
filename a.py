sozluk = {"CRINGE": "Garip ya da utandirici bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşilik cevap",
            "SHEESH": "onaylamamak"
            }
kelime = input("bir kelime giriniz: ")

if kelime in sozluk.keys():
    print(sozluk[kelime])

else:
    print("kelime bulunamadi!")

