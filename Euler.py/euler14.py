def kontrol(x):
    if x % 2 == 0:
        return x/2
    else:
        return (3*x)+1

def steps(x):
    step=1
    while True:
        x=kontrol(x)
        step+=1
        if x ==1:
            return step

max_steps=0

champ_number=0

for number in range(1,1000001):
    aux = steps(number)
    if aux > max_steps:
        max_steps=aux
        champ_number=number

print(champ_number)
print(max_steps)







