# fibonacci sayilari 1,2,3,5,8,13...

#kendinden onceki 2 sayinin toplami
#4 000 000 kucuk fibonacci sayilarindan cift olanlarin toplami kactir?
#
#

# ---------------------------liste ile cozum
list=[1,2]


i=2
while True:
    if list[i-1]+list[i-2]<4000000:
        list.append(list[i-1]+list[i-2])
        i+=1
    else:
        break
sum=0
for j in list:
    if j % 2==0:
        sum+=j

print(sum)



# ------------------------------a+b=c , a=b , b=c mantiksal cozum

a = 1
b = 2
sum = 2
while True:
    c = a + b

    a = b

    b = c

    if c%2==0:

        sum+=c

    if c>4000000:
        break

print(sum)






































