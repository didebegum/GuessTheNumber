import random

sayiList = []
tahminEdilen=0

basamak = input("Kaç basamaklı sayı tahmin etmek istersiniz?")
basamakSayi = int(basamak)

while len(sayiList) != basamakSayi: 
    sayi = random.randint(0,9)
    if str(sayi) in sayiList:
        print("")
    else:
        sayiList.append(str(sayi))

while tahminEdilen != sayiList:
    tahminEt= input("Sayı tahmin ediniz: \n")
    tahminEdilen = list(tahminEt)

    for i in range(basamakSayi):
        if sayiList[i-1] == tahminEdilen[i-1]:
            print("+")
        
    for a in range(basamakSayi):
        if tahminEdilen[a-1] in sayiList:
            if sayiList[a-1] != tahminEdilen[a -1]:
                print("-")
