def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a//b


def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi=="toplama":
        return f1(5,5)
    elif islem_adi=="cikarma":
        return f2(10,5)
    elif islem_adi=="carpma":
        return f3(5,5)
    elif islem_adi=="bolme":
        return f4(25,5)
    else:
        print("hatali islem yapmayi denediniz...")

result=islem(toplama,cikarma,carpma,bolme,"bolme")
print(result)
