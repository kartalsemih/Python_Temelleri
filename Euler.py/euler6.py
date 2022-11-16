

def kareAlma(num):
    return num**2

def dogalSayiToplami(num2):
    sum = 0
    for i in range(1,(num2+1)):
        sum += i
    return sum



list = []
for i in range(1,101):
    list.append(kareAlma(i))

kareleriToplami = sum(list)



kendiToplami = dogalSayiToplami(100)
kendiToplamiKaresi = kareAlma(kendiToplami)



result = kendiToplamiKaresi - kareleriToplami
print(result)


