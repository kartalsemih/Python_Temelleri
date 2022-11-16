# ınheritance (kalıtım):miras alma

#person => name , lastname ,age ,eat(),run(),drink()
#student(person),teacher(person) => 

#animal => dog(animal),cat(animal





class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname 

        print("Person Created")

    def who_am_i(self):
        print("i am a person")

    def eat(self):
        print("i am eating")

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentnumber=number
        print("Student Created")

    # override
    def who_am_i(self):
        print("i am a student")

    def SayHello(self):
        print("hello i am a student")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch=branch

    def who_am_i(self):
        print(f"i am a {self.branch} teacher")

p1=Person("ali","yılmaz")
s1=Student("çınar","turan",5555)
t1=Teacher("Serkan","yılmaz","math")

print(p1.firstname + " " + p1.lastname)
print(s1.firstname + " " + s1.lastname + " " + str(s1.studentnumber))


p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.SayHello()
t1.who_am_i()
