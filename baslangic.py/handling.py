from ast import Raise
from logging import exception


# try:
#     x=int(input("x:"))
#     y=int(input("y:"))
#     print(x/y)
# except Exception as ex :
#     print(f"y için 0 girilemez.Sebebi {ex}")

# en çok kullanacağım "Exception" tüm hataların classı as ex diyerek hata sebebi görülebilir




# x=10
# if x>5:
#     raise Exception("x 5 den büyük değer alamaz ")



# def check_password(psw):
#     import re
#     if len(psw)<8:
#         raise Exception("parola en az 8 karakter olmalıdır")
#     elif not re.search("[a-z]",psw):
#         raise Exception("parola küçük harf içermelidir")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("parola büyük harf içermelidir")
#     elif not re.search("[0-9]",psw):
#         raise Exception("parola rakam içermelidir")
#     elif not re.search("[_@$]",psw):
#         raise Exception("parola alpha numeric karakter  içermelidir")
#     elif re.search("\s",psw):
#         raise Exception("parola boşluk içermemelidir")
#     else:
#         print("geçerli parola")



# password=("12345678aA_")

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola: else"),
# finally:
#     print("validation tamamlandı")


# class Person():
#     def __init__(self,name,year):
#         if len(name)>10:
#             raise Exception("name alanı fazla karakter içeriyor")
#         else:
#             self.name=name
            

# p=Person("aliiiiiiiiiiii",1989)




