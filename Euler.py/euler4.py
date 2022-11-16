





def check_palindromik(num):
    stringNum = str(num)

    newString = stringNum[::-1]

    if int(newString) == num:
        return True
    else:
        return False

biggiest_palondromik = 0


for i in range(100,1000):
    for j in range(100,1000):
        if check_palindromik(i*j):
            if i*j > biggiest_palondromik:
                biggiest_palondromik = i*j
                continue
            else:
                continue



print(biggiest_palondromik)













































