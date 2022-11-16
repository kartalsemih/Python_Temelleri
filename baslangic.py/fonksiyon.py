# def yaşhesaplama (yaş):
#     return (2022-yaş)

# yaşgirdisi=(yaşhesaplama-1992)

# print(yaşgirdisi)

def sayhello(name='user'):
  return 'hello '+name

msg=sayhello('çınar')
msg=sayhello('ada')
print(msg)


def total(num1,num2):
    return num1+num2

result=total(10,20)
result=total(15,20)
print(result)


def yashesapla(dogumyili):
    return 2022-dogumyili

agecinar=yashesapla(2017)
ageada=yashesapla(2010)
agesena=yashesapla(1999)
print(agecinar,ageada,agesena)

def emekliligekacyilkaldi(dogumyili,isim):

    '''
    DOCSTRING: dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: dogum yili
    OUTPUT: hesaplanan yil bilgisi

    '''

    yas=yashesapla(dogumyili)
    emeklilik=65-yas

    if emeklilik>0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('zaten emekli oldunuz')


emekliligekacyilkaldi(1983,'ali')
emekliligekacyilkaldi(1950,'çinar')
emekliligekacyilkaldi(1974,'ziya')



print(help(emekliligekacyilkaldi))

list=[1,2,3]
print(help(list.append))
