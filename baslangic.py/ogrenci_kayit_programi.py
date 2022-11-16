# ad-soyad bilgisi istenecek
# 3 tane not istenecek
# bilgileri dosyaya kayıt edilecek
# not ortalamasını dosyadan çekerek istenildiğinde gösterilecek 
# 100-90 AA , 89-85 BA,80-84 BB,79-75 CB,65-74 CC,60-64 DC,55-59 DD,50-54 FD,0-49 FF


# isim=input("isim:")
# soyisim=input("soyisim:")
# not1=(input("not1:"))
# not2=(input("not2:"))
# not3=(input("not3:"))
   
    
# #ortalama=(not1+not2+not3)/3
# with open("ogrenciUygulama","a",encoding="utf-8")as file:
#     file.write(isim+" "+soyisim+":"+not1+","+not2+","+not3+"\n")
    

# print("bilgileriniz alındı")

# while True:
#     enter=input("isminiz:")
#     password=input("soyisminiz:")
#     break

# AA=100>=90
# BA=89>=85
# BB=80>=84
# CB=79>=75
# CC=65>=74
# DC=60>=64
# DD=55>=59
# FD=50>=54
# FF=0>=49


# if isim==enter:
#     if password==soyisim:
#         with open("ogrenciUygulama","r",encoding="utf-8")as file:
#             result=file.read()
#             print(result)
#     else:
#         print("soyisim yanlış")
# else:
#     print("isim yanlış")
import os


def ortalamaHesap(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenciAdi=liste[0]
    
    notlar=liste[1].split(",")
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama=(not1+not2+not3)/3

    if ortalama>=90 and ortalama<=100:
        harf="AA"
    elif ortalama>=85 and ortalama<=89:
        harf="BA"
    elif ortalama>=65:
        harf="CC"
    else:
        harf="FF"

    return ogrenciAdi+": "+harf+"\n"

    







def NotGir():
    name=input("isim:")
    surname=input("soyisim:")
    while True:
        not1=int(input("not1:"))
        if not1<=100:
            break
        else:
            print("notunuz 100'den az olmalı")
    while True:
        not2=int(input("not2:"))
        if not2<=100:
            break
        else:
            print("notunuz 100'den az olmalı")
    while True:
        not3=int(input("not3:"))
        if not3<=100:
            break
        else:
            print("notunuz 100'den az olmalı")

    with open("notlar.txt","a",encoding="utf-8")as file:
        file.write(name+" "+surname+":"+str(not1)+","+str(not2)+","+str(not3)+"\n")
        print("-"*25)
        print("Notlar Girildi")
        print("-"*25)


def NotlarıOku():
    try:
        with open("notlar.txt","r",encoding="utf-8")as file:
            print("-"*25)
            for satir in file:
                print(ortalamaHesap(satir))
            print("-"*25)
    except FileNotFoundError:
        print("-"*25)
        print("Okunacak Not Yok") 
        print("-"*25)


        
            




def NotlarıKayıtEt():
    try:
        with open("notlar.txt","r",encoding="utf-8")as file:
            liste=[]
        
            for i in file:
                liste.append(ortalamaHesap(i))
        with open("sonuclar.txt","w",encoding="utf-8")as file2:
            for i in liste:
                file2.write(i)
        print("-"*25)
        print("Kayıt Başarılı")
        print("-"*25)
    except FileNotFoundError:
        print("-"*25)
        print("Kayıt Edilecek Not Yok") 
        print("-"*25)
    

def tumKayitlariGor():
    try:
        with open("sonuclar.txt","r",encoding="utf-8")as file:
            print("TÜM KAYITLAR".center(25,"-"))
            print(file.read())
            print("-"*25)
    except FileNotFoundError:
            print("-"*25)
            print("Gösterilecek Kayıt Yok")
            print("-"*25)

def tumKayitSil():
    try:
        os.remove("sonuclar.txt")
        os.remove("notlar.txt")
        print("-"*25)
        print("Tüm Kayıtlar Silindi")
        print("-"*25)
    except FileNotFoundError:
        print("-"*25)
        print("Silinecek Kayıt Yok") 
        print("-"*25)






def appIntro():
    q=("Uygulamaya Hoşgeldiniz")
    print(q.center(100,"*")+"\nLütfen Yapmak İstediğiniz İşlemi Seçiniz...")


appIntro()
while True:
    print("1-Notları Oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n5-Tüm Kayıtları Sil\n6-Tüm Kayıtları Gör")
    
    enter=input("")

    if enter =="1":
        NotlarıOku()
    elif enter=="2":
        NotGir()
    elif enter=="3":
        NotlarıKayıtEt()
    elif enter=="5":
        tumKayitSil()
    elif enter=="6":
        tumKayitlariGor()
    else:
        j="Hoşçakalın"
        print(j.center(100,"*"))
        break







