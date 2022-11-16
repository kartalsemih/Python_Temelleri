# key - value

# 41 => kocaeli 34 => istanbul

#sehirler = ['Kocaeli','Istanbul']
#plakalar = [41, 34]

#print(plakalar[sehirler.index('Kocaeli')])

#plakalar = { 'balıkesir':10,'istanbul':34}
#print(plakalar['balıkesir'])
#print(plakalar['istanbul'])

"""
users = { 
         'semih kartal':{
            'age': 30,
            'address':'balıkesir',
            'mail':'inciinciq@gmail.com'
         }
          
    
}
print(users['semih kartal']['age'])

"""
"""
ogrenciler = {
    '120':{
        'ad':'ali',
        'soyad':'yılmaz',
        'telefon':'532 000 00 01',
    },
    '125':{
        'ad':'can',
        'soyad':'korkmaz',
        'telefon':'532 000 00 02',

    },
    '128':{
        'ad':'volkan',
        'soyad':'yükselen',
        'telefon':'532 000 00 03',
    },

}
"""
"""
ogrenciler = {}

number = input('öğrenci no:')
name = input('öğrenci adı:')
surname = input('öğrenci soyadı:')
phone = input('telefon no:')

#ogrenciler[number] = {
#    'ad':name,
#    'soyad':surname,
#    'phone':phone,
#}


#print(ogrenciler)

ogrenciler.update({
    number : {
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})

number = input('öğrenci no:')
name = input('öğrenci adı:')
surname = input('öğrenci soyadı:')
phone = input('telefon no:')

ogrenciler.update({
    number : {
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})

number = input('öğrenci no:')
name = input('öğrenci adı:')
surname = input('öğrenci soyadı:')
phone = input('telefon no:')

ogrenciler.update({
    number : {
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})

print(ogrenciler)

ogrNo = input('öğrenci no:')
ogrenci = ogrenciler[ogrNo]

print(ogrenci)














        

                

"""
