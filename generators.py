def kup():
    for i in range(5):
        yield i**3

for i in kup():
    print(i)