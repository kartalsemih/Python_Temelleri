

sayı=int(input('sayı: '))
asalmı=True


if sayı ==1:
    asalmı=False
for i in range(2,sayı):
    if (sayı%i==0):
         asalmı=False
         break

if asalmı:
    print('sayı asaldır')
else:
    print('sayı asal değildir')

# i=2
# while True:
#     if sayı==1:
#         print("asal değildir")
#         break
#     if sayı%i==0:
#         if i==sayı:
#             print("asal sayıdır")
#             break
#         else:
#             print("asal değildir")
#             break
#     i+=1


# if sayı==1:
#     print("asal değil")
    

# for i in range(2,sayı+1):
#         if sayı%i==0:
#             if i==sayı:
#                 print("asal")
#                 break
#             else:
#                 ("asal değil")
#                 break
    


