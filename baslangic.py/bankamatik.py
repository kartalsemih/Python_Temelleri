# bankamatik uygulaması

semihhesap={
    'ad':'semih kartal',
    'hesap no':'1565165',
    'bakiye':3000,
    'ek hesap': 2000

}

alihesap={
    'ad':'ali kartal',
    'hesap no':'15659555',
    'bakiye':2000,
    'ek hesap': 1000

}

def paracek(hesap,miktar):
    print(f"merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye']-=miktar
        print('paranızı alabilirsiniz')
        bakiyesorgula(hesap)
    else:
        toplam=hesap['bakiye']+hesap['ek hesap']

        if (toplam >= miktar):
            ekhesapkullanımı=input('ek hesap kullanılsın mı (e/h) ?')

            if ekhesapkullanımı=='e':
                ekhesapkullanılacakmiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ek hesap']-=ekhesapkullanılacakmiktar
                print('paranızı alabilirsiniz')
                bakiyesorgula(hesap)
            else:
                print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyesorgula(hesap)



def bakiyesorgula(hesap):
    print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.ek hesap limitiniz {hesap['ek hesap']} TL dir.")


paracek(semihhesap,3000)

print('***************')

paracek(semihhesap,2000)

