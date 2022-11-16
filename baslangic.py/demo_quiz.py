# # question


# class question():
#     print("Quiz uygulamasına hoşgeldiniz".center(100,'*'))
#     toplamPuan=100
#     soru1= int(input("soru 1: 2 + 2 ="))
#     if (soru1==4):
#         print("doğru cevap")
#         toplamPuan-=0
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10  
#     soru2= int(input("soru 1: 2 + 3 ="))
#     if (soru2==5):
#         print("doğru cevap")
#         toplamPuan-=0
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     soru3= int(input("soru 1: 2 + 4 ="))
#     if (soru3==6):
#         print("doğru cevap")
#         toplamPuan-=0
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     soru4= int(input("soru 1: 2 + 5="))
#     if (soru4==7):
#         print("doğru cevap")
#         toplamPuan-=0 
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     soru5= int(input("soru 1: 2 + 6 ="))
#     if (soru5==8):
#         print("doğru cevap")
#         toplamPuan-=0  
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     soru6= int(input("soru 1: 2 + 7 ="))
#     if (soru6==9):
#         print("doğru cevap")
#         toplamPuan-=0 
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     soru7= int(input("soru 1: 2 + 8 ="))
#     if (soru7==10):
#         print("doğru cevap")
#         toplamPuan-=0 
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     soru8= int(input("soru 1: 2 + 9="))
#     if (soru8==11):
#         print("doğru cevap")
#         toplamPuan-=0
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     soru9= int(input("soru 1: 2 + 10 ="))
#     if (soru9==12):
#         print("doğru cevap")
#         toplamPuan-=0
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     soru10= int(input("soru 1: 2 + 11 ="))
#     if (soru10==13):
#         print("doğru cevap")
#         toplamPuan-=0 
#     else:
#         print("yanlış cevap")
#         toplamPuan-=10 
#     print(f"quiz bitti,aldığınız puan: {toplamPuan}")



        


# #quiz

# quiz=question()



# questions

class Questions:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def CheckAnswer(self,answer):                                          # 1 cevap değişkeni self.cevap ile eşit mi yani doğru mu diye kontrol etme methodu oluşturdu
        return self.answer==answer


q1=Questions("En iyi programlama dili hangisidir?",["C#","Python","Javascript","Java"],"Python")
q2=Questions("En popüler programlama dili hangisidir?",["Java","C#","Python","Javascript"],"Python")
q3=Questions("En çok kazandıran programlama dili hangisidir?",["Javascript","C#","Java","Python"],"Python")
questions=[q1,q2,q3]
#quiz

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0                                                            # score ihtiyaci olduğu için score tanımlandı ve 0 olarak başladı
        self.questionIndex=0                                              # yukarıdan alınan soru listesinin index sayısına göre soru çağrılacağı için index no oluşturuldu ve 0 olarak başladı
    def getQuestions(self):                                             # 1.method) yukarıdaki class dan soruyu getirme methodu ,sıfırıncı indexini getirdi
        return self.questions[self.questionIndex]
    def displayQuestion(self):                                         # 2.method) soruyu gösterme methodu soru1: yazdırıp ulaştığı sorunun text ini yazdırdı ve yukarıdaki şıkları döngüyle 
        question=self.getQuestions()                               
        print(f"Soru {self.questionIndex+1}: {question.text}")

        for q in question.choices:                                       # 2 sorunun altına şık olarak yazdırdı
            print("-"+q)

        answer=input("cevap:")                                          # 2 cevap istedi 
        self.guess(answer)                                                  # 2 cevabı guess methodunda çalıştırdı
        self.loadQuestion()                                                 # 2 soru yükleme (sonraki soru) methodunu çalıştırdı

    def guess(self,answer):                                               # 3.method) tahmin methodu oluşturdu  
        question=self.getQuestions()                                # 3 soru getir methoduna soru değişkeni atandı

        if question.CheckAnswer(answer):                         # 3 sorudan üst class daki cevap kontrol methodu çağırıldı ve içine cevap koyuldu 
            self.score+=1                                                     # 3 cevap true dönerse score 1 arttırıldı
        self.questionIndex+=1                                           # 3 cevap true yada false ne dönerse dönsün soru index i 1 arttırılıp kendine eşitlendi

    def loadQuestion(self):                                              # 4 .method)soru yükleme methodu oluşturuldu sonraki soruya geçme işine yarıyor
        if len(self.questions)==self.questionIndex:            # 4 eğer yukarıdan alınan soru listesindeki eleman sayısı ile listeden soru alma işine yarayan index sayısı eşit ise
            self.showScore()                                                 # 4 score göster methodu döndürüldü
        else:
            self.displayprogress()                                          #4 soru sayısı ile soru index i eşit değil ise displayprogress methodu döndürüldü
            self.displayQuestion()                                         #4 ardından 2.method yani soru göster methodu çağırıldı

    def showScore(self):                                                   # 5.method) score gösterme methodu oluşturuldu
        print("Score: ",self.score)                                         # 5 score ekranda yazdırıldı

    def displayprogress(self):                                            #6.method) displayprogress methodu oluşturuldu
        totalquestions=len(self.questions)                          #6 soru listesindeki soru sayısı değişkene atandı
        questionnumber=self.questionIndex+1                  #6 index sayısı +1 verilerek soru numarasına atandı

        if questionnumber>=totalquestions:                         #6 eğer soru numarası toplam soru sayısından büyükse 
            print("quiz bitti")                                                  #6 quiz bitti yazıdırılır
        else:
            print(f"question {questionnumber} of {totalquestions}".center(100,"*"))  #soru numarası toplam soru sayısından küçük ise soru başlığı yazdırılır





quiz=Quiz(questions)

quiz.loadQuestion()
















