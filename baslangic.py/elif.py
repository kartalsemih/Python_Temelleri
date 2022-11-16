# x = int(input('x: '))
# y = int(input('y: '))

# if x > y :
#     print('x y den büyük')
# elif x == y :
#     print('x y eşit')
# else :
#     print('y x den büyük')

# num = int(input('sayı: '))

# if num > 0 :
#     print('sayı pozitif')
# elif num < 0 : 
#     print('sayı negatif')
# else :
#     print('sayı sıfır')

# name = input('isim: ')
# age = int(input('yaş: '))
# eğitim = input('eğitim: ')

# if age >=18:
#     if (eğitim == 'lise') or (eğitim == 'üniversite'):
#         print('ehliyet alabilir')
#     else:
#         print('eğitim durumundan dolayı ehliyet alamaz')
# else:
#     print('yaş durumundan dolayı ehliyet alamaz')

# yazılı1= float(input('1.yazılı: '))
# yazılı2= float(input('2.yazılı: '))
# sözlü=float(input('sözlü: '))

# ortalama= (((yazılı1+yazılı2)/2)+(sözlü))/2
# print('*'*100)
# print(f"not ortalamanız: {ortalama}")

# if (ortalama >= 0) and (ortalama <= 24):
#     print('notunuz 0')
# elif (ortalama >= 25) and (ortalama <= 44):
#     print('notunuz 1')
# elif (ortalama >= 45) and (ortalama <= 54):
#     print('notunuz 2')
# elif (ortalama >= 55) and (ortalama<=69):
#     print('notunuz 3')
# elif (ortalama>=70) and (ortalama<=84):
#     print('notunuz 4')
# elif (ortalama>=85)and(ortalama<=100):
#     print('notunuz 5')




# import datetime


# bugün = datetime.datetime.today()

# doğumgünü = datetime.datetime(2023,5,16)

# print(bugün-doğumgünü)

# çıkış tarihi: 2018,8,1




import datetime




trafiğe_çıkış= (input('trafiğe çıkış tarihi: '))
trafiğe_çıkış=trafiğe_çıkış.split('/')

giriş_tarihi = datetime.datetime(int(trafiğe_çıkış[0]),int(trafiğe_çıkış[1]),int(trafiğe_çıkış[2]))

bugün = datetime.datetime.now()

fark=bugün-giriş_tarihi
print(fark.days)








# if (trafiğe_çıkış>=0)and(trafiğe_çıkış<=365):
#     print('1.servis yılı')
# elif (trafiğe_çıkış>= 366)and(trafiğe_çıkış<=(365*2)):
#     print('2.servis yılı')
# elif (trafiğe_çıkış>=((365*2)+1))and(trafiğe_çıkış<=(365*3)):
#     print('3.servis yılı')
# elif (trafiğe_çıkış>=((365*3)+1))and(trafiğe_çıkış<=(365*4)):
#     print('4.bakım yılı')
# else:
#     print('arabanız çok eski')









 





   





        
    
  


    








