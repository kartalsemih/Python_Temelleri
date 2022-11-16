

import time
import math


baslangic = time.time()
def asalMi(num):


    sonuc = True


    if num == 2 :
        return sonuc
    else:
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                sonuc = False
                break
        return sonuc

asalSayiListesi = []
index = 2
while True:
    if asalMi(index):
        asalSayiListesi.append(index)
        index += 1
        if len(asalSayiListesi) == 10001:
            break
    else:
        index += 1
        if len(asalSayiListesi) == 10001:
            break

print(asalSayiListesi[-1])

bitis = time.time()

print(bitis-baslangic)











































