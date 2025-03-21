
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                               DATE TIME
#*----------------------------------------------------------------------------------------------------------------------------------------


from datetime import date

bugun = date.today()
# print(bugun)                                     #*     Çıktı: 2025-02-28
# print(type(bugun))                               #*     Çıktı: <class 'datetime.date'>
# print(bugun.day)                                 #*     Çıktı: 28
# print(bugun.month)                               #*     Çıktı: 2
# print(bugun.year)                                #*     Çıktı: 2025
# print(bugun.weekday())                           #*     Çıktı: 4  -->  Haftanın 4. günü demektir. Günler 0'dan başlar.
# print(bugun.isoweekday())                        #*     Çıktı: 5  -->  Haftanın 5. günü demektir. Günler 1'den başlar.

# gecmis_tarih = date(2015,8,13)
# gecen_zaman = bugun - gecmis_tarih
# print(gecen_zaman)                               #*     Çıktı: 3487 days, 0:00:00 sadece date işlemi yaptığımız için saat 00:00:00 geldi.


#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                               DATE TIME 
#?----------------------------------------------------------------------------------------------------------------------------------------

from datetime import datetime

suan = datetime.now()
# print(suan)                                      #?     Çıktı: 2025-02-28 13:38:35.775411
# print(type(suan))                                #?     Çıktı: <class 'datetime.datetime'>
# print(suan.ctime())                              #?     Çıktı: Fri Feb 28 13:54:17 2025
# print(suan.date())                               #?     Çıktı: 2025-02-28
# print(suan.time())                               #?     Çıktı: 13:56:30.894953
# print(suan.year)                                 #?     Çıktı: 2025
# print(suan.month)                                #?     Çıktı: 2
# print(suan.day)                                  #?     Çıktı: 28
# print(suan.hour)                                 #?     Çıktı: 13
# print(suan.minute)                               #?     Çıktı: 52
# print(suan.second)                               #?     Çıktı: 15

# gecmis_an = datetime(2014,5,26,6,45,32,123)
# print(suan - gecmis_an)                          #?     Çıktı: 3931 days, 7:15:34.681810


# print(bugun.strftime("%d-%m-%Y-%A"))             #?     Çıktı: 28-02-2025-Friday
# print(suan.strftime("%d-%m-%Y-%A"))              #?     Çıktı: 28-02-2025-Friday


#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                            TIME DELTA
#TODO-------------------------------------------------------------------------------------------------------------------------------------

from datetime import timedelta

# tdelta = timedelta(days = 7, hours = 5, seconds =69)
# print(suan + tdelta)                             #TODO  Çıktı: 2025-03-07 19:15:00.677696  -->  Bulunduğumuz zamanın üstüne girdiğimiz parametre kadar ekledik
# print(suan - tdelta)                             #TODO  Çıktı: 2025-02-21 09:12:42.677696  -->  Bulunduğumuz zamanın üstüne girdiğimiz parametre kadar çıkardık


#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                 1901'DEN 2000'E KADAR HER AYIN 1'DE KAÇ DEFA PAZAR GUNUNE DENK GELIR
#!----------------------------------------------------------------------------------------------------------------------------------------

pazar_sayisi = 0
for yil in range(1901,2001):
    for ay in range(1,13):
        if datetime(yil,ay,1).weekday() == 6:    #!     Her yılın her ayını tek tek dönerken 1. günü alıp onunda gün sayısını çıkarıp 6 ile eşit mi onu kontrol ediyoruz.
            pazar_sayisi += 1
print(pazar_sayisi)                              #!     Çıktı: 171

#!----------------------------------------------------------------------------------------------------------------------------------------
