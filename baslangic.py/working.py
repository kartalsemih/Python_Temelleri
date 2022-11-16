

# name = input('isminiz: ')
# age = int(input('yaşınız: '))
# education = input('eğitim durumunuz: ')

# if (age >= 18) :
#     if ((education == 'lise') or (education == 'üniversite')):
#         print('ehliyet alabilir')
#     else:
#         print('eğitim durumu yetersiz') 
# else:
#     print('yaş durumu yetersiz')


# yazılı_1 = int(input('yazılı 1: '))
# yazılı_2 = int(input('yazılı 2: '))
# sözlü    = int(input('sözlü: '))

# average  = (yazılı_1 + yazılı_2 + sözlü)/3

# print('*'*100)

# print(f"not ortalamanız:{average.__round__(2)}")

# if (average <= 24):
#     print('notunuz 0')
#     print('*'*100)
# elif (average >= 25) and (average <= 44):
#     print('notunuz 1')
#     print('*'*100)
# elif (average >= 45 ) and (average <= 54):
#     print('notunuz 2')
#     print('*'*100)
# elif (average >= 55) and (average <= 69):
#     print('notunuz 3')
#     print('*'*100)
# elif (average >= 70) and (average <= 84):
#     print('notunuz 4')
#     print('*'*100)
# elif (average >= 85) and (average <= 100):
#     print('notunuz 5')
#     print('*'*100)
# else:
#     print('YANLIŞ BİLGİ GİRDİNİZ')   
#     print('*'*100)




# import datetime


# bugün = datetime.datetime.now()


# çıkış = input('aracınızın trafiğe çıkış tarihi: ')
# ayır = çıkış.split('/')


# tarih = datetime.datetime(int(ayır[0]),int(ayır[1]),int(ayır[2]))
# fark = bugün - tarih

# print(f"aracınız trafiğe {fark.days} gün önce çıkmıştır")

# print('*'*100)

# if (fark.days <= 365):
#     print('1.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days >= 366) and (fark.days <= 365*2):
#     print('2.servis yılı içindesiniz')
# elif(fark.days >= 366) and (fark.days <= 365*2):
#     print('2.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days > 365*2) and (fark.days <= 365*3):
#     print('3.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days > 365*3) and (fark.days <= 365*4):
#     print('4.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days > 365*4) and (fark.days <= 365*5):
#     print('5.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days > 365*5) and (fark.days <= 365*6):
#     print('6.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days > 365*6) and (fark.days <= 365*7):
#     print('7.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days > 365*7) and (fark.days <= 365*8):
#     print('8.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days > 365*8) and (fark.days <= 365*9):
#     print('9.servis yılı içindesiniz')
#     print('*'*100)
# elif(fark.days > 365*9) and (fark.days <= 365*10):
#     print('10.servis yılı içindesiniz')
#     print('*'*100)
# else:
#     print('ARACINIZ 10 YAŞINDAN BÜYÜKTÜR')
#     print('*'*100)


sayı = int(input('sayı: '))

if (sayı >= 0) and (sayı <100):
    print('sayı 0 ile 100 arasındadır')
else:
    print('sayı 0 ile 100 arasında değildir')

sayı = int(input('sayı: '))

if (sayı > 0) :
    if (sayı % 2 == 0):
        print('sayı pozitif çift sayı')
    else:
        print('sayı pozitif ancak çift sayı değil')
else:
    print('sayı pozitif  değil')

email = 'kartalsemih@windowslive.com'
password = '1234'

login = input('mail gir: ')
passwordgir = input('password gir: ')

if (login.strip().lower() == email) :
    if (passwordgir.strip().lower()==password):
        print('giriş başarılı')
    else:
        print('password yanlış')
else:
    print('mail yanlış')

num1 = int(input('sayı1: '))
num2 = int(input('sayı2: '))
num3 = int(input('sayı3: '))


if (num1 > num2) and (num1 > num3):
    print('1.sayı en büyüktür')
elif (num2 > num1) and (num2 > num3):
    print('2.sayı en büyüktür')
elif (num3 > num1) and (num3 > num2):
    print('3.sayı en büyüktür')
else:
    print('hatalı bilgi')


vize1 = int(input('1.vize: '))
vize2 = int(input('1.vize: '))
final = int(input('final: '))

ortalama = ((((vize1+vize2)/2)*60)/100)+(final*40/100)

print(f'ortalamanız: {ortalama}')


if (final>=70):
    print("'final 70 den büyük' geçti")
elif (ortalama >= 50):
    if (final>=50):
        print(f'{ortalama} ortalama ile geçti')
    else:
        print("'final 50 den düşük' kaldı")
else: 
    print("'ortalama 50 den düşük' kaldı")

ad = input('adınız: ')
kilo= int(input('kilonuz: '))
boy=float(input('boyunuz: ') )


indeks = kilo/boy**2

print('*'*100)

print(f'vücut kitle indeksiniz:{indeks.__round__(2)} ')

print('ve')



if (indeks <= 18.4):
    print('zayıfsınız')
    print('*'*100)
elif (indeks >=18.5 ) and (indeks <= 24.9):
    print('normalsiniz')
    print('*'*100)
elif (indeks >=25 ) and (indeks <= 29.9):
    print('fazla kilolusunuz')
    print('*'*100)
elif (indeks >=30 ) and (indeks <= 100):
    print('obezsiniz')
    print('*'*100)
else:
    print('hatalı bilgi girdiniz')
    print('*'*100)











    




    












    


























