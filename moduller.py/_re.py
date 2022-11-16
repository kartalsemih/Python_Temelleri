import re

# arama islemleri
# regex - regular expression islemler *?-_\$%&#'!


result = dir(re)
# re module

str = "Python kursu : Python programlama Rehberiniz | 40 saat"

# re.findall()

# result = re.findall("Python",str)
# result = len(result)

# result = re.split(" ",str)
# result = re.split("R",str)

# re.sub()
# \s = bosluk karakteri
# result = re.sub(" ","-",str)

# re.search()

result = re.search("Python",str)

# result = result.span()
#result = result.start()
#result = result.end()
#result = result.group()
#result = result.string



# regular expression

#result = re.findall("[abc]",str)
#result = re.findall("[saat]",str)

result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)

#"[0-39]" = ["01239"]
# [^abc] = abc disindaki tum karakterleri arar
# [^0-9] = rakam olmayan tum karakterler

# . = herhangi bir karakteri ifade eder
# .. = a = no match
#      ab = 1 match
#      abc = 1 match
#      abcd = 2 match

result = re.findall("...",str)

# ^a = belirtilen karakter ile basliyor mu
# ^a = a = 1 match
#      abc = 1 match
#      fgc = no match


# $ = belirtilen karakter ile bitiyor mu
# a$ = a = 1 match
# a$ = lamba = 1 match
# a$ = python = no match

# * = bir karakterin sifir yada daha fazla sayida olmasini kontrol eder
# ma*n = mn = 1 match
#        man = 1 match
#        maaaan = 1 match
#        main = no match

# + = bir karakterin bir yada daha fazla sayida olmasini kontrol eder
# ma+n = mn = no match
#        man = 1 match
#        maaaan = 1 match
#        main = no match ( a nin arkasindan n gelmiyor)

# ? = bir karakterin sifir yada bir kere olmasini kontrol eder

# {} = karakter sayisini kontrol eder
# al{} = a karakterinin arkasina l karakteri 2 kez tekrarlamali
# al{2,3} = a karakterinin arkasina l karakteri en az 2 en fazla 3 kez tekrarlamali
# [0-9]{2,4} = en az 2 en cok 4 basamakli sayilar

# | = alternetif seceneklerden birinin gerceklesmesi gerekir
# a|b = a yada b
#     cde = no match
#     ade = 1 match
#     acdbea = 3 match

# () = gruplama yapmak icin
# (a|b|c)xz  = a b c karakterlerinin herhangi birinin  arkasina xz gelmelidir

# \ = ozel karakterleri aramamizi saglar
#  \$a = $ karakterinin arkasina a karakterini arar yani $ regular expression engine tarafindan yorumlanmaz
# \A = belirtilen karakter stringin basinda mi
# \Athe = the stringin basinda mi
#\Z = belirtilen karakter stringin sonunda mi
# the\Z = the stringin sonunda mi
# \b = belirtilen karakter kelimenin basinda yada sonunda mi
# \bthe = the kelimenin basinda mi
# the\b = the kelimenin sonunda mi
# \B = belirtilen karakter kelimenin basinda yada sonunda degil mi
# the\B = the kelimenin sonunda degil mi
#\Bthe = the kelimenin basinda degil mi
# \d = [0-9] ayni anlama gelir yani rakamlari arar
# \D = [^0-9] ayni anlama gelir yani rakam olmayanlari arar


# \s = bosluk karakterlerini arar
# \S  = bosluk karakterleri disindakiler
# \w = alfabetik karakterler , rakamlar ve _(alt cizgi) karakteri
# \W = \w nun tam tersi






print(result)







