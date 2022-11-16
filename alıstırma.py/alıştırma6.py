import random
import colorama
from colorama import Fore, Back, Style
colorama.init()



sayı=random.randint(1,10)

print(Fore.LIGHTMAGENTA_EX)
hak= int(((input('kaç hak istiyorsunuz?: '.title())))) 


puan=100
can=hak
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input('tahmininiz: '.title()))
    if (tahmin==sayı):
        print(Fore.GREEN)
        print(f'tebrikler {sayac} defada bildiniz!,puanınız {100-(puan/can)*sayac-1}'.title())
        print('-'*10)
        break
    elif tahmin<sayı:
        print(Fore.LIGHTYELLOW_EX)
        print(f'yükselt!'.title())
        print('-'*10)
    else:
        print(Fore.BLUE)
        print(f'düşür!'.title())
        print('-'*10)

if (hak==0)and(tahmin!=sayı):
    print(Fore.RED)
    print(f'hakkınız bitti.tutulan sayı {sayı}')



# if (hak==0)and(tahmin!=sayı):
#     print('hakkınız bitti! tutulan sayı:',sayı)
           
# list=[]
# for i in range(1,6):
#     list
    
# print(list)


#  sayı=int(input('sayı giriniz: '))   
# a=True
# i=1

# if sayı==1:
#     a=False
# while i<sayı:
#     i+=1
#     if sayı%i==0:
#         a=False
#     break
    

# if a:
#     print('asal sayıdır.')
# else:
#     print('asal sayı değildir.')

# soru=int(input('kaç müşteri gireceksiniz?: '))


# list=[]
# i=0
# while i<soru:
#     müşteriadı=input('müşteri adı: ')
#     müşterinumarası=input('müşteri numarası: ')
#     müşteriyaşı=input('müşteri yaşı: ')
#     list.append(((müşteriadı,müşteriyaşı,müşterinumarası)))
#     i+=1

# # müşteriler= {
# #     'müşteri adı': müşteriadı,
# #         'müşteri numarası:':müşterinumarası,
# #         'müşteri yaşı:': müşteriyaşı
# # }


# i=[x for x in range(0,1000,10) ]
# print(i[78])



    

  





    


























