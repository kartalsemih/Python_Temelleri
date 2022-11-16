# class


class Person:

    #class attributes
    adress='no information'



    # constructor(yapıcı metod)
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.year=year
        print('init methodu çalıştı')


    # instance methods

    def intro(self):
        print("Hello There "+ self.name)

    def calculateAge(self):
        return 2022-self.year


    

# object (instance)

p1=Person(name='ali',year=1990)
p2=Person(name='yağmur',year=2005)

# updating
p1.name='ahmet'
p1.adress='kocaeli'




# accessing object attributes


print(f"p1: name: {p1.name} year: {p1.year} adress: {p1.adress} ")
print(f"p1: name: {p2.name} year: {p2.year} adress: {p2.adress} ")


p1.intro()
p2.intro()

print(f"Adım: {p1.name} ve Yaşım: {p1.calculateAge()} ")
print(f"Adım: {p2.name} ve Yaşım: {p2.calculateAge()} ")


class Circle:
    # class object attribute
    pi=3.14


    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    # methods

    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)


c1=Circle()  # yaricap=1
c2=Circle(5)

print(f"c1: Alan= {c1.alan_hesapla()} çevre= {c1.cevre_hesapla()}")
print(f"c1: Alan= {c2.alan_hesapla()} çevre= {c2.cevre_hesapla()}")





class Ogrenciler:

    def __init__(self,name,surname,age,nott):
        self.name=name
        self.surname=surname
        self.age=age
        self.nott=nott 


    def YasHesapla(self):
        return 2022-self.age
    


class Ogretmenler:
    maas=10000
    


class Calısanlar:
    maas=7500
    


O1=Ogrenciler("Semih","Kartal",30,75)

print(O1.name,O1.surname,O1.YasHesapla(),O1.nott)
print(O1.name,O1.surname,O1.age,O1.nott)

