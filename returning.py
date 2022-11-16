


# def usAlma(number):
#
#
#     def inner(power):
#         return number ** power
#
#     return inner
#
#
# two = usAlma(2)
# print(two(3))
# three = usAlma(3)
# print(three(4))

# def yetkiSorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolu {1} sayfasina ulasabilir".format(role,page)
#         else:
#             return "{0} rolu {1} sayfasina ulasamaz".format(role,page)
#
#     return inner
#
# user1 = yetkiSorgula("Product edit")
#
# print(user1("User"))

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

# toplama = islem("toplama")
# print(toplama(1,3,5,7,9,15,85,656,6,6156,156,11,651,6,165))

carpma = islem("carpma")
print(carpma(15,52,56,5,6,8,4,8,7))









