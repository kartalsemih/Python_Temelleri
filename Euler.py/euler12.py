



import math

def bolen_sayisi(x):
    bolen=1
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i ==0:
            bolen+=1
    return bolen*2


n=1
while True:
    number=(n*(n+1))/2
    if bolen_sayisi(number) > 500:
        print(int(number))
        break
    n+=1











