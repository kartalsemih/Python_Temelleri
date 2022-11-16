# def belirtilenkezekrandagösterme(kelime,adet):
#     return (kelime*adet)


# result=belirtilenkezekrandagösterme('Hello World\n',10)

# print(result)


# list=[]
# def parametreyilisteyeçevir(*params):
#     for i in params:
#         list.append(i)
    
#     return list

# result=parametreyilisteyeçevir('semih',25,True,39,'kartal,')
# print(result)


sayi1=int(input('sayi1: '))
sayi2=int(input('sayi2: '))
asalsayilar=[]
i=2
def asalsayibulma(sayi1,sayi2):
    if (sayi1<=1)or(sayi2<=1):
        False
    else:
        for y in range(sayi1,sayi2):
            i= i+1
            if (y%i==0):
                False
            else:
                asalsayilar.append(i)
    return asalsayilar

result=asalsayibulma(sayi1,sayi2)
print(result)



# def tambölenbulma(sayi):

#     tambölen=[]

#     for i in range(2,sayi):
#         if (sayi%i==0):
#             tambölen.append(i)
#     return tambölen

# sayi=int(input('sayi: '))

# result=tambölenbulma(sayi)
# print(result)








                








    
        
    
