# # and               => iki sorunun da doğru olması gerekiyor True bilgisi gelmesi için

# # or                => sadece bir soru doğru olsa bile True bilgisi gelir

# # not               => cevabın zıttını gösterir sonuç True ise False cevabı döndürür

# #---------------------------------------------------
# sayı = int(input('sayı giriniz: '))

# result = (sayı > 0) and (sayı <= 100)

# print(f"girdiğiniz sayı 0 ve 100 arasındadır: {result}")

# #---------------------------------------------------

# sayı = int(input('sayı giriniz: '))

# result = (sayı > 0) and (sayı %2 == 0)

# print(f"girdiğiniz sayı pozitif ve çift sayıdır: {result} ")

# #----------------------------------------------------

# mail = 'kartalsemih@windowslive.com'
# password = '12345'

# mail_gir = input('mailinizi giriniz: ')
# password_gir = input('password giriniz: ')

# result = (mail_gir == mail) and (password == password_gir)

# print(f"girdiğiniz mail adresi ve şifreniz doğrudur: {result}")

# #-----------------------------------------------------------

# sayı_1 = int(input("1.sayıyı giriniz: "))
# sayı_2 = int(input("2.sayıyı giriniz: "))
# sayı_3 = int(input("3.sayıyı giriniz: "))

# result = (sayı_1 > sayı_2) and (sayı_1 > sayı_3)
# result_2 = (sayı_2 > sayı_1) and (sayı_2 > sayı_3)
# result_3 = (sayı_3 > sayı_1) and (sayı_3 > sayı_2)

# print(f"girdiğiniz 1.sayı en büyük sayıdır: {result}")
# print(f"girdiğiniz 2.sayı en büyük sayıdır: {result_2}")
# print(f"girdğiniz 3.sayı en büyük sayıdır: {result_3}")

# #-------------------------------------------------------------


# vize_1 = int(input('1.vize notunuz: '))
# vize_2 = int(input('2.vize notunuz: '))
# final  = int(input('final notunuz: '))

# ortamala = (((vize_1 + vize_2) / 2 )*60/100) + ( final*40/100)

# geçti_kaldı = ((ortamala >= 50) and (final >= 50)) or (final >= 70)

# print(f"öğrenci not ortalaması:{ortamala} dersten geçmiştir: {geçti_kaldı}")

# #------------------------------------------------------

# ad = input('adınızı giriniz: ')
# kilo = float(input('kilonuzu giriniz: '))
# boy = float(input('boyunuzu giriniz: '))

# kilo_indeksi = kilo / (boy**2)

# zayıf = (kilo_indeksi >= 0) and (kilo_indeksi <= 18.4)
# normal = (kilo_indeksi >= 18.5 ) and (kilo_indeksi <= 24.9)
# fazla_kilolu = (kilo_indeksi >= 25) and (kilo_indeksi <= 29.9)
# şişman = (kilo_indeksi >= 30) and (kilo_indeksi <= 34.9)

# print('-'*100)



# print(f"girdiğiniz bilgilere göre vücut kitle indeksiniz: {kilo_indeksi.__round__(2)}")
# print('-'*100)
# print(f"ve genel vucut değerlendirme durumunuz zayıf :{zayıf} ")
# print(f"ve genel vucut değerlendirme durumunuz normal :{normal}")
# print(f"ve genel vucut değerlendirme durumunuz fazla kilolu:{fazla_kilolu} ")
# print(f"ve genel vucut değerlendirme durumunuz şişman :{şişman}")



































