from datetime import datetime
from datetime import timedelta

# tarih ve saat islemleri


# classlar
#      date  ==> tarih ile alakali islem yapilacagi zaman "date" class
#      datetime     ==> tarih ve zaman ile alakali birlesik islem yapilacagi zaman "time" class
#      time    ==> zaman ile alakali islem yapilacagi zaman "time" class
#      timedelta


x = datetime.now()

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

y = datetime.ctime(x)

print(y)

z = datetime.strftime(x,"%Y")    # ==> buyuk Y 2022,kucuk y 22,sadece yil bilgisi
z = datetime.strftime(x,"%X")    # ==> buyuk X saat bilgisi,kucuk x tarih bilgisi
z = datetime.strftime(x,"%d")    # ==> kucuk d sadece gun bilgisi buyuk D tarih bilgisi
z = datetime.strftime(x,"%A")     # ==> buyuk A sadece gun bilgisini string verir "Monday"
z = datetime.strftime(x,"%B")    # ==> buyuk B ay bilgisini string olarak verir "Novamber"
z = datetime.strftime(x,"%Y %B %A")   # ==> esnek sekilde bir arada kullanilabilirler
print(z)

t = "21 Nisan 2019"

gun , ay ,yil = t.split()

print(gun)
print(ay)
print(yil)


t = "15 April 2022 hour 10:12:30"
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")

time = dt.year

print(time)

birthday = datetime(1992,5,16,12,59,59)

print(birthday)

result = datetime.timestamp(birthday) # ==> verilen tarihten bugune kadarki zamani saniyeye cevirir
result = datetime.fromtimestamp(result)  # ==> saniyeyi tekrardan tarih datetime bilgisine cevirir
result = datetime.fromtimestamp(0)

result = x - birthday   # sonuc olarak timedelta objesi geliyor

# result = result.days
#result = result.seconds
#result = result.microseconds
print(x)
result = x + timedelta(days=730,minutes=10)

result = x - timedelta(days=10,minutes=20)

print(result)


videoYuklenmeTarihi = datetime(2020,3,10)

fark = x - videoYuklenmeTarihi

print(fark)














