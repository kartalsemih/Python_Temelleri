# import random
# x=random.randint(1,100)

# t=int(input('kaç tahminde bulursun?: '))
# puan=0
# i=1
# while i<=t:
#     y=int(input('tahmininiz: '))
#     if y == x:
#         print(f'tebrikler sayı bulundu.puanınız {}')
#     elif y<x:
#         print(f'yukarı')
#     elif y>x:
#         print(f'aşağı')   
#     i+=1
# print('hakkınız bitti')

import random
sayı=random.randint(1,10)
can=int(input('kaç hak kullanmak istersiniz: '))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input('tahmin: '))
    if tahmin==sayı:
        print(f'tebrikler {sayac}. defada bildiniz.toplam puanınız {(100-(100/can)*(sayac-1))}')
        break
    elif sayı>tahmin:
        print('yukarı')
    else:
        print('aşağı')
    if hak==0:
        print(f'hakkınız bitti.tutulan sayı:{sayı}')





    
