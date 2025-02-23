print("Merhaba Dünya")                           #  Çıktı: Merhaba Dünya
print('Merhaba Dünya')                           #  Çıktı: Merhaba Dünya
print("Ali'nin evi")                             #  Çıktı: Ali'nin evi
print('Ali\'nin evi')                            #  Çıktı: Ali'nin evi      -->  Eğer ki tek tırnak içinde string değerlerimizi yazarsak o metin içinde tekrar tek tırnak kullanmak istediğimizde metni kapattığımızı düşünmesin diye "\" işareti koyarız
#*----------------------------------------------------------------------------------------------------------------------------------------
print("""Merhaba                                 

Dünya""")
#*     Çıktı: 
#*     Merhaba
                                                 
#*     Dünya
#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
print('''Merhaba
      
Dünya''')
#?     Çıktı: 
#?     Merhaba

#?     Dünya
#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
print("Merhaba\nDünya")                          #TODO  "\n" --> alt satıra geç demek
#TODO  Çıktı: 
#TODO  Merhaba
#TODO  Dünya
#TODO------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
print("Merhaba\tDünya")                          #!     Çıktı: Merhaba Dünya  -->  Her bir "\t" işareti bir tab boşluk bırakıp devam eder. Ayarlarımızda tab kaç karakterse o kadar boşluk bırakır.
#!----------------------------------------------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------
mesaj1 = "Merhaba"
mesaj2 = "Dünya"
mesaj3 = "baş harfine bak"

print(mesaj1 + " " + mesaj2)                     #*     Çıktı: Merhaba Dünya
print(mesaj1[1])                                 #*     Çıktı: e
print(mesaj1[0:4])                               #*     Çıktı: Merh
print(mesaj1[2:])                                #*     Çıktı: rhaba
print(mesaj1[::2])                               #*     Çıktı: Mraa                 ilk parametre boş olduğu için baştan başladı. İkinci parametrede boş olduğu için sonuna kadar gidecek. Üçüncü parametrede 2 olduğu için ikişer ikişer ilerleyecek.
print(mesaj1[::-1])                              #*     Çıktı: abahreM
print(mesaj1 * 2)                                #*     Çıktı: MerhabaMerhaba
print(mesaj1.upper())                            #*     Çıktı: MERHABA
print(mesaj3.capitalize())                       #*     Çıktı: Baş harfine bak
print(mesaj1.startswith("me"))                   #*     Çıktı: False                Metin "me" ile başlıyor mu demek. Büyük küçük duyarlılığı var.
print(mesaj1.endswith("a"))                      #*     Çıktı: True
print(len(mesaj1))                               #*     Çıktı: 7                    Kaç karakter uzunluğuundadır demek
#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
isim = "Melih"
soyIsim = "Diler"
yas = 31

print("{} {} adlı üyemiz {} yaşındadır".format(isim,soyIsim,yas))  #*     Çıktı: Melih Diler adlı üyemiz 31 yaşındadır
print(f"{isim} {soyIsim} adlı üyemiz {yas} yaşındadır")            #*     Çıktı: Melih Diler adlı üyemiz 31 yaşındadır
#?----------------------------------------------------------------------------------------------------------------------------------------

