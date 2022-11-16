# x = 0

# while x < 22:
#     if (x == 1):
#         print(x)
#     elif (x == 3):
#         print(x)
#     elif (x == 5):
#         print(x)
#     elif (x == 7):
#         print(x)
#     elif (x == 9):
#         print(x)
#     elif (x == 12):
#         print(x)
#     elif (x == 19):
#         print(x)
#     elif (x == 21):
#         print(x)
#     x += 1


# başlangıç = int(input("başlangıç: "))
# bitiş = int(input('bitiş: '))

# i=başlangıç
# y=bitiş
# while i<y:
#     i+=1
#     if i%2!=0:
#         print(f'tek:{i}')


# sayılar=[1,3,5,7,9,12,19,21]
# i=0
# while i<len(sayılar):
#     print(sayılar[i])
#     i+=1
# başlangıç=int(input('başlangıç: '))
# bitiş=int(input('bitiş: '))

# while başlangıç<bitiş:
#     if başlangıç%2!=0:
#         print(başlangıç)
#     başlangıç+=1
   
# i=100
# while i>0:
#     print(i)
#     i-=1
# numbers=[]
# i=0
# while i<5:
#     sayı=int(input('sayı: '))
#     numbers.append(sayı)
#     numbers.sort()
#     i+=1
# print(numbers)




ürünler=[]
adet=int(input('ürün sayısı: '))

i=0
while i<adet:
    ürünadı=input('ürün adı: ')
    ürünfiyatı=input('ürün fiyatı: ')
    ürünler.append({
        'ürün adı': ürünadı,
        'ürün fiyatı': ürünfiyatı
    })
    i+=1
for ürün in ürünler:
    print(f'ürün adı: {ürün["ürün adı"]} ürün fiyatı: {ürün["ürün fiyatı"]}')









