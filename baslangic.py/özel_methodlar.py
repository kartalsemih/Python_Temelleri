mylist=[1,2,3]
# mystring="my string"
# print(len(mylist))
# print(len(mystring))

class movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie objesi oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    def __del__(self):
        print("obje silindi")

    

       

m=movie("film adı","film yönetmeni",120)

# print(str(mylist))
print(str(m))
# print(len(mylist))
#print(len(m))






#print(m.title,m.director,m.duration)

#print(len(m))

# print(type(mylist))
# print(type(mystring))
# print(type(m))