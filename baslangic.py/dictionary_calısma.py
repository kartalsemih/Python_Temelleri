öğrenciler = {}

number = input('öğrenci no: ')
name = input('öğrenci adı: ')
surname = input('öğrenci soyad: ')
phone = input('öğrenci telefon: ')

#öğrenciler[number] = {
#    'ad':name,
#    'soyad':surname,
#    'telefon':phone
#}

öğrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }

})

number = input('öğrenci no: ')
name = input('öğrenci adı: ')
surname = input('öğrenci soyad: ')
phone = input('öğrenci telefon: ')

öğrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }

})

number = input('öğrenci no: ')
name = input('öğrenci adı: ')
surname = input('öğrenci soyad: ')
phone = input('öğrenci telefon: ')

öğrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }

})

ogrnO = input('öğrenci no: ')
ogrenci = öğrenciler[ogrnO]
print('*'*50)



print(f"aradığınız {ogrnO} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")



