
import time
import math


baslangic=time.time()


def asalMi(num):


    if num == 2:
        return True

    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False

    return True






sum =0
index = 2
while True:
    if asalMi(index):
        sum +=index
        if index == 2000000:
            break
        index+=1
    else:
        if index==2000000:
            break
        index+=1

print(sum)

bitis=time.time()

print(bitis-baslangic)





