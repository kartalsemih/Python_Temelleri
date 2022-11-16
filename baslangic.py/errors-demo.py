list=["1","2","5a","10b","abc","50","60"]

for q in list:
    try:
        int(q)==int
    except Exception as ex:
        continue

    print(q)


# password=input("şifre:")
# if  password  ("ğ" , "Ğ", "ç", "Ç", "ş", "Ş", "ü", "Ü", "ö", "Ö", "ı", "İ" ):
#     print("şifre türkçe karakter içermemeli")
# try:    
#     quit=input("çıkış için 'q' tuşuna basınız:")
#     if quit=="q":
#         print("çıkış başarılı")
#     else:

# except Exception as ex:
#     print(ex)
