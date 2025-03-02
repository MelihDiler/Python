
#      getcwd = gecerli klasoru gostirir.
#      chdir = klasor degistirir.
#      listdir = klasorleri listeler.

#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                                GETCWD
#*----------------------------------------------------------------------------------------------------------------------------------------

import os

print(os.getcwd())                               #*     Cikti: C:\VS CODE\PYTHON  -->  Projemin bulundugu klasor
os.chdir("C:/Users/diler/Desktop/Python OS")     #*     Secili klasoru degistirir. Islemleri artik bu klasor uzerinden yapariz. Dosya yolu kopyaladiginda / yerine \ olarak gelir ve hata verir o sebeple bu sekilde degistirdik. Diger bir sekilde ise basina r koyarakda yapabilirdik. Or: r"C:\Users\diler\Desktop\Python OS" çünkü \ karakteri özel bir karakterdir mesela \n enter, \t tab demektir. adresteki \ karakterinin özel bir anlamı olmadığını söylemeye yarıyor.
print(os.getcwd())                               #*     Cikti: C:\Users\diler\Desktop\Python OS  -->  Bir ust satirda sectigim klasor.

#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                                LISTDIR
#?----------------------------------------------------------------------------------------------------------------------------------------

print(os.listdir())                              #?     Cikti: ['Deneme 1', 'Deneme 2', 'Deneme 3', 'Deneme 4', 'Deneme 5']  -->  Secili klasor icindekileri siralar.
print(os.listdir(r"C:\VS CODE\PYTHON"))          #?     Ben suan "C:/Users/diler/Desktop/Python OS" klasorunun icindeyim fakat parametre olarak baska bir klasor yolu verdim ve bana onu siraladi. Cikti: ['.git', '00 - Syntax.py', '01 - Stringler.py', '02 - Operatorler.py', '03 - Listeler.py', '04 - Demet (Tuple).py', '05 - Kümeler (Sets).py', '06 - Sözlükler (Dictionaries).py', '07 - If Dongusu.py', '08 - For Dongusu.py', '09 - While Dongusu.py', '10 - Input.py', '11 - Fonksiyonlar.py', '12 - Moduller.py', '13 - Random.py', '14 - Time.py', '15 -Date Time.py', '16 - OS.py', 'benim_modulum.py', '__pycache__']

for dosya in os.listdir():
    print(dosya)                                 #?     Cikti: Alt alta -->  Deneme 1 / Deneme 2 / Deneme 3 / Deneme 4 / Deneme 5  -->  Goruldugu gibi ust satidaki parametreyi degil hala secili klasoru getiriyor.

#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                              MKDIR
#TODO-------------------------------------------------------------------------------------------------------------------------------------

# os.mkdir("Yeni Klasor Olusturuldu")              #TODO  Cikti: Secili dosyada "Yeni Klasor Olusturuldu" adli klasor olusturduk. Tekrar calistirirsan ayni isimden oldugu icin hata verir.


#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                                MAKEDIRS
#!----------------------------------------------------------------------------------------------------------------------------------------

os.makedirs("Deneme Ic Ice 1/Deneme Ic Ice 2/Deneme Ic Ice 3")  #!     Bu isimlerde ic ice klasorler olusturduk. Tekrar calistirdiginda ayni isimden klasorler oldugu icin hata verir.

#!----------------------------------------------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                                 RMDIR
#*----------------------------------------------------------------------------------------------------------------------------------------

# os.rmdir("Deneme Ic Ice 1")                      #*     Bu koddan hata aliriz cunku rmdir sadece bos dizinleri silebilir. Dizin icinde dosya veya baska bir klasor varsa silemez.
# os.rmdir("Yeni Klasor Olusturuldu")              #*     "Yeni Klasor Olusturuldu" klasorunu sildi.

#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                              REMOVEDIRS
#?----------------------------------------------------------------------------------------------------------------------------------------

# os.removedirs("Deneme Ic Ice 1/Deneme Ic Ice 2/Deneme Ic Ice 3")  Tum klasorleri siler fakat mac'de sadece son klasoru siler cunku mac'de gorunmeyen gizli klasor olusturur ve bu komut sadece bos klasorleri sildigi icin en son klasoru siler digerlerinde gizli dosya vardir.

#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                              
#TODO-------------------------------------------------------------------------------------------------------------------------------------



#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                               
#!----------------------------------------------------------------------------------------------------------------------------------------



#!----------------------------------------------------------------------------------------------------------------------------------------
