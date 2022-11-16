import os
import datetime

# isletim sistemi islemleri


result = dir(os)
result = os.name
result = os.getcwd()
#os.chdir()
# os.mkdir("newdirectory")
# os.makedirs("C:\\newdirectory/yeniklasor")
# result = os.listdir()

# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

result = os.stat("date.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)   #olusturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)   # son erisilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)   # degistirilme tarihi
# os.system("notepad.exe")

# os.rename("newdirectory","yeniKlasor")
#os.rmdir("newdirectory")
#os.removedirs("yeniKlasor/yeniklasor")

result = os.path.abspath("_os.py")
result = os.path.dirname("/moduller.py/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("/")
result = os.path.isdir("/") # klasor mu
result = os.path.isfile("/")  #dosya mi
result = os.path.join("C:\\","deneme")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")





print(result)