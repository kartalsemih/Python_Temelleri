


#   (write)  w  modu 

#   (append)   a  modu

#     ( create)    x   modu 

#     (read)    r   modu


#     utf-8   turkce karakter destekli encoding

# file.seek(18)   dosyada kursoru istedigimiz konuma gondermek icin kullanilir
# file.tell()   dosyada kursorun o anki konumunu gosterır

#  w modu dosyayı silip oluşturup sıfırdan yazar

# file = open("open_file.txt","w")
# file.write("Semih Kartal")
# file.close()



#a modu dosyayı silmez üzerine kürsörün olduğu yerden devam eder

# file = open("open_file.txt","a")
# file.write("Semih Kartal\n")
# file.close()


# x modu yeni dosya oluşturur istenirse birşey yazılır , aynı isimli dosya varsa hata verir

# file = open("new_file.txt","x")
# file.write("Semih Kartal")
# file.close()





# file = open("open_file.txt","r")

# for i in file:
#     print(i,end="")

# result = file.read()                boş  birakirsan hepsini okur

# print(result)

# result = file.read(5)            kaç yazarsan  o kadar karakter okur

# print(result)

# print(file.readline(),end="")           #bos birakirsan ilk satiri okur,kac kere alt alta yazarsan o kadar satir gosterir
# print(file.readline(),end="") 
# print(file.readline(),end="")  

# print(result)

# result = file.readlines()

# print(result[5],end="")

# with open("open_file.txt","r",encoding="utf-8")as file:

#     result=file.read()

#     print(result)
#     file.seek(18)
#     print(file.tell())


file=open("newfile.txt","w",)
file.write("Semih Kartal\nAynur Kartal\nSibel Kartal")
file.close()

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content="izzet ali kartal\n"+content
#     file.seek(0)
#     file.write(content)


# with open("newfile.txt","a",encoding="utf-8")as file:
#     file.write("\nİzzet Ali Kartal")

# with open("newfile.txt","r+",encoding="utf-8")as file:
#     list=file.readlines()
#     list.insert(2,"İzzet Ali Kartal\n")
#     file.seek(0)
#     for i in list:
#         file.write(i)

with open("newfile.txt","r+",encoding="utf-8")as file:
    list=file.readlines()
    list.insert(2,"İzzet Ali Kartal\n")
    file.seek(0)
    file.writelines(list)


with open("newfile.txt","r",encoding="utf-8")as file:
    print(file.read())
 

