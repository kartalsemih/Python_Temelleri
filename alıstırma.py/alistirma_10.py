# 1/2 ,2/3, 3/4 ,4/5 ,5/6 ,7/8 ,8/9 ,9/10

# yukarıdaki bilgileri ekrana yazdırınız



# def startApp():
#     i=0
#     while i<9:
#         i+=1     
#         if i==6:
#             continue
#         print(f"{i}/{i+1}")

# """
# i=0 değişkenini atadık
# while döngüsü belli bir koşulu sağlayan durumlarda koşul kadar döngü üretir
# i 9 dan küçükmü diye soruyor yani 0 9 dan küçük mü sonuç evet ise döngü çalışıyor , hayır ise yani 9<9 olduğunda döngü duruyor
# küçük ise i=i+1 yapıyor yani 0=0+1 yeni "i"=1 oluyor
# if (eğer) i==6 yani i 6 ya eşit ise "continue" yani yapılacak işlemi o turda pas geç bir sonrakinden devam et diyoruz
# i 6 ya gelene kadar i==6 olmadığı için "continue" çalışmıyor ve alttaki çıktı ekranda gösteriliyor.
# f string ile i yani {i}1 "/" {i+1}2 , sonuç 1/2 gösteriliyor
# gösterim tamamlandıktan sonra döngü başa dönüyor i 9 dan küçük mü diye soruyor yani 1 9 dan küçük mü diyor sonuç evet 
# sonra i+=1 oluyor 1=1+1 yeni "i" 2 oluyor
# i==6 if i dönüyor 2==6 değil o zaman {i}2 "/" {i+1}3 , sonuç 2/3 gösteriliyor




# """        
            
    

    
        
    

# startApp()

# adim_sayisi2=[]
# cinsiyet2=[]

# def AdimSayisiAlma():
#     adim_sayisi=int(input("Adım sayınızı giriniz:"))
#     adim_sayisi2.append(adim_sayisi)
    
    


# def CinsiyetAlma():
#     cinsiyet=input("Cinsiyetinizi giriniz:")
#     cinsiyet2.append(cinsiyet)



     

# def KaloriHesapla():
#     global adim_sayisi2
#     global cinsiyet2
#     AdimSayisiAlma()
#     CinsiyetAlma()
#     if cinsiyet2[0]==("Kadın".lower().strip()) or ("Kadin".lower().strip()):
#         print((adim_sayisi2[0]*30)/500)
#     elif cinsiyet2[0]==("Erkek".lower().strip()):
#         print((adim_sayisi2[0]*45)/500)
#     else:
#         print("yanlış bilgi girdiniz")



# KaloriHesapla()


# def KaloriHesaplama():
#     adım_giriniz=int(input("adım giriniz:"))
#     cinsiyet=input("cinsiyet giriniz:").strip().lower()
    

#     if cinsiyet=="Kadın".strip().lower() or cinsiyet=="kadin".strip().lower():
#         print((adım_giriniz*30)/500)
#     elif cinsiyet==("Erkek".strip().lower()):
#         print((adım_giriniz*45)/500)
#     else:
#         print("yanlış bilgi girdiniz")

# KaloriHesaplama()


# makine_sayisi=int(input("makine sayısı:"))
# ay=int(input("ay:"))

# if ay>2 and ay<9:
#     çalışma_süresi=480
#     aralık_değeri=45
# else:
#     çalışma_süresi=540
#     aralık_değeri=30
# i=0
# while i<makine_sayisi:
#     i+=1
#     print(f"{i} .makine çalışma süresi: {çalışma_süresi}")
#     çalışma_süresi-=aralık_değeri






# sonbaharKis=(9,10,11,12,1,2)

# ilkbaharYaz=(3,4,5,6,7,8)

# makineSayisi=int(input("Makine Sayısı:"))

# ay=int(input("Kaçıncı Ay:"))

# sayac=0

# calisma=0

# while sayac<makineSayisi:

#     if ay in sonbaharKis:

#         mesai=(17-8)*60

#         print(f"{sayac+1}.Makine Çalışma Süresi:{mesai-calisma}")

#         calisma+=30

#         sayac+=1

#     elif ay in ilkbaharYaz:

#         mesai = (17 - 9) * 60

#         print(f"{sayac + 1}.Makine Çalışma Süresi:{mesai - calisma}")

#         calisma += 45

#         sayac += 1 





# class Sorular:
#     def __init__(self,soru,şık,cevap):
#         self.soru=soru
#         self.şık=şık
#         self.cevap=cevap
#     def CevapKontrol(self,cevap):
#         return self.cevap==cevap
# s1=Sorular("5+5",[10,20,30],10)
# s2=Sorular("10+10",[20,30,40],20)
# s3=Sorular("20+20",[40,50,60],40)
# sorulistesi=[s1,s2,s3]

# class Sınav():
#     def __init__(self,sorulistesi):
#         self.sorulistesi=sorulistesi
#         self.skor=0
#         self.sayaç=0
#     def SoruÇek(self):
#         return self.sorulistesi[self.sayaç]
#     def SoruGöster(self):
#         print(f"soru {self.sayaç+1} of {len(self.sorulistesi)}".center(50,"*"))
#         gelensoru=self.SoruÇek()
#         print(f"soru.{self.sayaç+1}: {gelensoru.soru}")
#         for i in gelensoru.şık:
#             print("-"+str(i))
#         cevap=int(input("cevap:"))
#         if gelensoru.CevapKontrol(cevap):
#             self.skor+=1
#         self.sayaç+=1
#         self.SonrakiSoru()
#     def SonrakiSoru(self):
#         if len(self.sorulistesi)<=self.sayaç:
#             print("sınav bitti")
#             print(f"skorunuz:{self.skor}")
#         else:
#             self.SoruGöster()
#     def SkorGöster(self):
#         print(f"skorunuz:{self.skor}")




    




# sınav=Sınav(sorulistesi)
# sınav.SoruGöster()



# i=0
# while range(i,10):
#     i+=1
#     print(f"{i}/{i}")
    
    

# 1/1,
# 2/2,
# 3/3,
# 4/4
# 5/5,
# 6/6,
# 7/7,
# 8/8,
# 9/9,
# 10/10



 #sayilar=[1,3,5,7,9,12,19,21]
# for i in sayilar:
#     if i%3==0:
#         print(i**2)






# toplam=0
# for i in sayilar:
#     toplam+=i


# print(toplam)


# sehirler=["kocaeli","istanbul","ankara","izmir","rize"]

# for i in sehirler:
#     if len(i)<=5:
#         print(i)


# ürünler = [
#     {'name':'samsung s6','price':'3000'},
#     {'name':'samsung s7','price':'4000'},
#     {'name':'samsung s8','price':'5000'},
#     {'name':'samsung s9','price':'6000'},
#     {'name':'samsung s10','price':'7000'}
# ]


# for i in ürünler:
#     x=int(i["price"])
#     if x <=5000:
#         print(i["name"])






# name=""    # boş iken false 
# while not name:  #not name=true boş iken true tekrar sor , 
#     name=input("isminizi giriniz:").strip()   # dolarsa true olur , not name = false olur sormayı durdurur.
    
# print(f"Merhaba,{name}")




# sayilar=[1,3,5,7,9,12,19,21]
# i=0
# while i<len(sayilar):
        
#         print(sayilar[i])
#         i+=1
#         if i== len(sayilar):
#             break
        
# baslangic=int(input("başlangıç:"))
# bitiş=int(input("bitiş:"))

# while baslangic<bitiş+1:
    
#     if baslangic%2==1:
#         print(baslangic)
#     baslangic+=1



# q=100
# while 0<q:
    
#     print(q)
#     q-=1


# i=0
# list=[]


# while i<5:
#     x=input("sayi:")
#     list.append(x)
#     i+=1
#     list.sort()
    
# print(list)


# list=[]
# i=0
# adet=int(input("adet:"))

# while i<adet:
#     ürünadi=input("ürün adi:")
#     ürünfiyatı=input("fiyatı:")
#     list.append({
#         "ürün adi:":ürünadi,
#         "ürün fiyatı:":ürünfiyatı
#     })
#     i+=1

# i=0
# while i<len(list) :
#     print(list[i]["ürün adi:"] +" fiyatı :" +list[i]["ürün fiyatı:"] + "TL")
#     i+=1
    

# i=-1
# while i<5:
#     i+=1
#     if i==2:
#         continue
#     print(i)

# toplam=0
# i=0
# q=100
# while i<=100:
#     if i%2==1:
#         toplam+=i
#     i+=1
    

# print(toplam)



# result=[x if x%2==0 else "tek"  for x in range(2,10)  ]
# print(result)
    
# import random

# seçilen_Sayi=random.randint(0,10)
# puan=100
# tahmin=int(input("kaç tahminde bulunacaksınız:"))
# i=0
# sayac=0
# while i<tahmin:
#     i+=1
#     sayac+=1

#     sayi=int(input("sayi giriniz:"))
#     if sayi==seçilen_Sayi:
#         puan-=0
#         print(f"{sayac} defada bildiniz")
#         print(puan)
#         break
#     if sayi<seçilen_Sayi:
#         puan=puan-(100/tahmin)
#         print("yukarı")
#         if i==tahmin:
#             print(f"hakkınız bitti sayı {seçilen_Sayi} idi\npuan:{0}")
#     elif sayi>seçilen_Sayi:
#         puan=puan-(100/tahmin)
#         print("aşağı")
#         if i==tahmin:
#             print(f"hakkınız bitti sayı {seçilen_Sayi} idi\npuan:{0}")
    
    

# sayi=int(input("sayi giriniz:"))
# i=0


# q=[x for x in range(0,100,5)]

# print(q[1:])
# class s():

#     def semih():


# def Topla(i,q):
#     return i+q

# x=Topla(50,50)
# print(x)


# def displayScreen(word,howmanytimes):
#     return word*howmanytimes


# q=displayScreen("Semih Kartal \n",5)


# print(q)


# def convertToList(*args):
#     return list(args)


# q=convertToList(10,20,30,"Semih",True,99)

# print(q)


# def findPrimeNumbers(sayi1,sayi2):
#     z=[]
#     for i in range(sayi1,sayi2+1):
#         if i >1:
#             for q in range(2,i):
#                 if i%q==0:
#                     break
#             else:
#                 z.append(i)
#     return z

        

# y=findPrimeNumbers(5,11)
# print(y)


# def findexactdivisor(sayi):
#     exact_divisor=[]
#     i=2
#     while i<sayi:
#         if sayi%i==0:
#             exact_divisor.append(i)
#         i+=1
#     return exact_divisor

# q=findexactdivisor(10)
# print(q)






# class Sorular():
#     def __init__(self,soru,şık,cevap):
#         self.soru=soru
#         self.şık=şık
#         self.cevap=cevap
#     def cevapKontrol(self,cevap):
#         return self.cevap==cevap

# s1=Sorular("2+2","a-3\nb-4\nc-5","b")
# s2=Sorular("5+5","a-10\nb-20\nc-30","a")
# s3=Sorular("10+10","a-30\nb-10\nc-20","c")
# sorular=[s1,s2,s3]

# class Sınav(Sorular):
#     def __init__(self,sorular):
#         self.sorular=sorular
#         self.index=0
#         self.score=0
#     def soruGetir(self):
#         return self.sorular[self.index]
#     def sınavBaşlığı(self):
#         question=self.soruGetir()
#         totalQuestions=len(self.sorular)
#         print(f"question {self.index+1} of {totalQuestions}".center(100,"*"))
#         print(f"{self.index+1}.soru:{question.soru} ")
#         şıklar=self.sorular[self.index]
#         print(şıklar.şık)
#         cevap=input("cevabınız:")
#         if question.cevapKontrol(cevap):
#             self.score+=1
#         self.index+=1
#         if self.index==totalQuestions:
#             print(f"sınav bitti skorunuz {self.score}")
#         else:
#             self.sınavBaşlığı()
# sınav=Sınav(sorular)
# sınav.sınavBaşlığı()







        


    
    
        
        

