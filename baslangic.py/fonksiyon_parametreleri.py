# def changename(n):
#     n ='ada'
# name='yiğit'

# changename(name)
# print(name)

# def change(n):
#     n[0]='istanbul'

# sehirler=['ankara','izmir']

# change(sehirler[:])

# print(sehirler)
# n=sehirler[:]

# n[0]='İstanbul'
# print(sehirler)
# print(n)


# def add(*params):
#     print(params[2])
#     return sum((params))

# result=add(5,5,90,50,88,78,62,5,8,7,8,9,5,5,21,5,169,187,415,154,1,651,54)
# print(result)


def add(*params):
    print(type(params))
    sum=0

    for i in params:
        sum = sum+i

    return sum
    
result=add(5,5,90,50,88,78,62,5,8,7,8,9,5,5,21,5,169,187,415,154,1,651,54)
print(result)

def displayuser(**params):
    print(type(params))
    for key,value in params.items():
        print(' {} is {} '.format(key,value))


displayuser(name='çınar',age=2,city='istanbul')
displayuser(name='ada',age=12,city='kocaeli',phone='1231231')
displayuser(name='yiğit',age=14,city='ankara',phone='12123121',email='yigit@gmail.com')


def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50,key1='value1',key2='value2')
