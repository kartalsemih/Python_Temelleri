



#   "2510" 1den 10a kadar olan sayilarin herbirine kalansiz bolunen en kucuk sayidir.
#    1'den 20'ye kadar olan sayıların tamamına tam bölünebilen en küçük pozitif sayı kaçtır ?


import time





baslangic = time.time()

def check1_20(num):
    i = 2
    while True:
        if num % i == 0:
            if num % (i+1) == 0:
                if num %(i+2) == 0:
                    if num%(i + 3) == 0:
                        if num%(i + 4) == 0:
                            if num%(i + 5) == 0:
                                if num%(i + 6) == 0:
                                    if num%(i + 7) == 0:
                                        if num%(i + 8) == 0:
                                            if num % (i + 9) == 0:
                                                if num % (i + 10) == 0:
                                                    if num % (i + 11) == 0:
                                                        if num % (i + 12) == 0:
                                                            if num % (i + 13) == 0:
                                                                if num % (i + 14) == 0:
                                                                    if num % (i + 15) == 0:
                                                                        if num % (i + 16) == 0:
                                                                            if num % (i + 17) == 0:
                                                                                if num % (i + 18) == 0:
                                                                                    return True
                                                                                else:
                                                                                    return False
                                                                            else:
                                                                                return False
                                                                        else:
                                                                            return False
                                                                    else:
                                                                        return False
                                                                else:
                                                                    return False
                                                            else:
                                                                return False
                                                        else:
                                                            return False
                                                    else:
                                                        return False
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False






sayi = 0
i = 1
while True:
    if check1_20(i):
        sayi = i
        break
    else:
        i += 1

print(sayi)

bitis = time.time()

print(bitis - baslangic)
















