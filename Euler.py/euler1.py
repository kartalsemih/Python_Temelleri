#1000 den kucuk 3'e ve 5'e bolunen butun sayilarin toplami kactir


list = []
for i in range(1,1000):
    if (i % 3 == 0) or (i % 5 == 0):
        list.append(i)



sum=0
for q in list:
    sum+=q

print(sum)







