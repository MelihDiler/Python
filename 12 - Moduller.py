#      Python'da modüller, belirli bir işlevi yerine getiren fonksiyonlar, değişkenler ve sınıflar içeren dosyalardır.
#      Örneğin bir sayının karesini hesaplayan fonksiyonu yazmak yerine hazır fonksiyonu import ederek direkt kullanabiliriz.
#      import os  --> işletim sistemiyle ilgili işlemler yapabileceğin modul
#      import time  -->  saat kaç? bir programın çalışması ne kadar sürdü? program belirli bir süre uyku moduna geçsin gibi işlemler
#      import datetime  -->  tarihle ilgili işlemler

#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                                 
#*----------------------------------------------------------------------------------------------------------------------------------------

import math                                      #*     Matematik modülünü dahil ettik

sonuc = math.factorial(5)                        #*     Bu modül içindeki faktöriyel fonksiyonunu çalıştırdık.
print(sonuc)                                     #*     Çıktı: 120

#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                    TUM MATEMATIK MODULUNU IMPORT ETMEDEN SADECE IHTIYACINI IMPORT ETME
#?----------------------------------------------------------------------------------------------------------------------------------------

from math import factorial, sqrt

sonuc2 = factorial(5)                            #?     Matematik modülünün tamamını import etmediğimiz için direkt factorial'i çağırdık.
print(sonuc2)                                    #?     Çıktı: 120

sonuc3 = sqrt(4)
print(sonuc3)                                    #?     Çıktı: 2  -->  4'ün karekökü 2'dir.

#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                KENDI OLUSTURDUGUM MODULU CAGIRMA
#TODO-------------------------------------------------------------------------------------------------------------------------------------

import benim_modulum                             #TODO  Ya da from benim_modulum import cember_cevresi

sonuc4 = benim_modulum.cember_cevresi(4)
print(sonuc4)                                    #TODO  Çıktı: 25.12

#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                            
#!----------------------------------------------------------------------------------------------------------------------------------------




#!----------------------------------------------------------------------------------------------------------------------------------------
