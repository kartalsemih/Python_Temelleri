# hesap1={
#     'ad':'semih kartal',
#     'hesap no':'1122233',
#     'bakiye':5000,
#     'ek bakiye':2500
# }

# hesap2={
#     'ad':'sibel kartal',
#     'hesap no':'445566',
#     'bakiye':7500,
#     'ek bakiye':5000
# }

# hesap3={
#     'ad':'aynur kartal',
#     'hesap no':'778899',
#     'bakiye':10000,
#     'ek bakiye':7500
# }








# def paraçekme(hesap):
#     print(f"sayın {hesap['ad']} hoşgeldiniz!".title().center(100,'*'))
#     işlemseçme=(int(input(f"para çekme 1\nbakiye sorgulama 2\nyapmak istediğiniz işlem: ")))
#     print('-'*50)

#     if (işlemseçme==1):
#         çekim=int(input("çekmek istediğiniz tutarı giriniz: "))
#         if hesap['bakiye']>=çekim:
#             print('para çekme işlemi başarılı')
#             hesap['bakiye']-=çekim
#         elif (hesap['bakiye']+hesap['ek bakiye'])>=çekim:
#             print(f"çekmek istediğiniz tutar ({çekim}) bakiyenizden ({hesap['bakiye']}) fazladır.\nek bakiye kullanmak için 1 çıkmak için 2 giriniz")
#             ekbakiyesorma=int(input('yapmak istediğiniz işlem: '))
#             if (ekbakiyesorma==1):
#                 print('para çekme işlemi başarılı')
#                 toplam=çekim-hesap['bakiye']
#                 hesap['ek bakiye']-=toplam
#                 hesap['bakiye']=0
#             elif (ekbakiyesorma==2):
#                 print(f"bakiyeniz {hesap['bakiye']}TL\nek bakiyeniz {hesap['ek bakiye']}TL\nbizi tercih ettiğiniz için teşekkür ederiz")
#         else:
#             print(f"bakiye yetersiz")
#     elif (işlemseçme==2):
#         print(f"bakiyeniz {hesap['bakiye']}TL\nek bakiyeniz {hesap['ek bakiye']}TL")
#         print('-'*50)



# paraçekme(hesap2)
# paraçekme(hesap2)



        

   













hesap1={
    'ad':'semih kartal',
    'hesap no':'112233',
    'şifre':'şifre1',
    'bakiye':5000,
    'ek bakiye':2500
}

hesap2={
    'ad':'sibel kartal',
    'hesap no':'445566',
    'şifre':'şifre2',
    'bakiye':7500,
    'ek bakiye':5000
}

hesap3={
    'ad':'aynur kartal',
    'şifre':'şifre3',
    'hesap no':'778899',
    'bakiye':10000,
    'ek bakiye':7500
}


giriş=input('hesap no giriniz: ').strip().lower()
şifre=input('şifre giriniz: ').strip().lower()

if giriş==hesap1['hesap no']:
    if şifre==hesap1['şifre']:
            print(f"sayın {hesap1['ad']} hoşgeldiniz!".title().center(100,'*'))
            işlemseçme=(int(input(f"para çekme 1\nbakiye sorgulama 2\nyapmak istediğiniz işlem: ")))
            print('-'*50)
            if (işlemseçme==1):
                çekim=int(input("çekmek istediğiniz tutarı giriniz: "))
                if hesap1['bakiye']>=çekim:
                                print('para çekme işlemi başarılı')
                                hesap1['bakiye']-=çekim
                elif (hesap1['bakiye']+hesap1['ek bakiye'])>=çekim:
                                print(f"çekmek istediğiniz tutar ({çekim}) bakiyenizden ({hesap1['bakiye']}) fazladır.\nek bakiye kullanmak için 1 çıkmak için 2 giriniz")
                                ekbakiyesorma=int(input('yapmak istediğiniz işlem: '))
                                if (ekbakiyesorma==1):
                                    print('para çekme işlemi başarılı')
                                    toplam=çekim-hesap1['bakiye']
                                    hesap1['ek bakiye']-=toplam
                                    hesap1['bakiye']=0
                                elif (ekbakiyesorma==2):
                                    print(f"bakiyeniz {hesap1['bakiye']}TL\nek bakiyeniz {hesap1['ek bakiye']}TL\nbizi tercih ettiğiniz için teşekkür ederiz")
                else:
                                print(f"bakiye yetersiz")
            elif (işlemseçme==2):
                print(f"bakiyeniz {hesap1['bakiye']}TL\nek bakiyeniz {hesap1['ek bakiye']}TL")
                print('-'*50)
    else:
        print('şifreniz yanlış')
elif giriş==hesap2['hesap no']:
    if şifre==hesap2['şifre']:
            print(f"sayın {hesap2['ad']} hoşgeldiniz!".title().center(100,'*'))
            işlemseçme=(int(input(f"para çekme 1\nbakiye sorgulama 2\nyapmak istediğiniz işlem: ")))
            print('-'*50)
            if (işlemseçme==1):
                çekim=int(input("çekmek istediğiniz tutarı giriniz: "))
                if hesap2['bakiye']>=çekim:
                                print('para çekme işlemi başarılı')
                                hesap2['bakiye']-=çekim
                elif (hesap2['bakiye']+hesap2['ek bakiye'])>=çekim:
                                print(f"çekmek istediğiniz tutar ({çekim}) bakiyenizden ({hesap2['bakiye']}) fazladır.\nek bakiye kullanmak için 1 çıkmak için 2 giriniz")
                                ekbakiyesorma=int(input('yapmak istediğiniz işlem: '))
                                if (ekbakiyesorma==1):
                                        print('para çekme işlemi başarılı')
                                        toplam=çekim-hesap2['bakiye']
                                        hesap2['ek bakiye']-=toplam
                                        hesap2['bakiye']=0
                                elif (ekbakiyesorma==2):
                                        print(f"bakiyeniz {hesap2['bakiye']}TL\nek bakiyeniz {hesap2['ek bakiye']}TL\nbizi tercih ettiğiniz için teşekkür ederiz")
                else:
                                print(f"bakiye yetersiz")
            elif (işlemseçme==2):
                print(f"bakiyeniz {hesap2['bakiye']}TL\nek bakiyeniz {hesap2['ek bakiye']}TL")
                print('-'*50)
    else:
        print('şifreniz yanlış')
elif giriş==hesap3['hesap no']:
    if şifre==hesap3['şifre']:
            print(f"sayın {hesap3['ad']} hoşgeldiniz!".title().center(100,'*'))
            işlemseçme=(int(input(f"para çekme 1\nbakiye sorgulama 2\nyapmak istediğiniz işlem: ")))
            print('-'*50)
            if (işlemseçme==1):
                çekim=int(input("çekmek istediğiniz tutarı giriniz: "))
                if hesap3['bakiye']>=çekim:
                                print('para çekme işlemi başarılı')
                                hesap3['bakiye']-=çekim
                elif (hesap3['bakiye']+hesap3['ek bakiye'])>=çekim:
                                print(f"çekmek istediğiniz tutar ({çekim}) bakiyenizden ({hesap3['bakiye']}) fazladır.\nek bakiye kullanmak için 1 çıkmak için 2 giriniz")
                                ekbakiyesorma=int(input('yapmak istediğiniz işlem: '))
                                if (ekbakiyesorma==1):
                                            print('para çekme işlemi başarılı')
                                            toplam=çekim-hesap3['bakiye']
                                            hesap3['ek bakiye']-=toplam
                                            hesap3['bakiye']=0
                                elif (ekbakiyesorma==2):
                                            print(f"bakiyeniz {hesap3['bakiye']}TL\nek bakiyeniz {hesap3['ek bakiye']}TL\nbizi tercih ettiğiniz için teşekkür ederiz")
                else:
                                print(f"bakiye yetersiz")
            elif (işlemseçme==2):
                print(f"bakiyeniz {hesap3['bakiye']}TL\nek bakiyeniz {hesap3['ek bakiye']}TL")
                print('-'*50)
    else:
        print('şifreniz yanlış')
else:
    print('hesap numaranız yanlış'.title())










