
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                          SOZLUK DICTIONARIES
#*----------------------------------------------------------------------------------------------------------------------------------------

#*     Sıralıdır.
#*     Anahtarlar tekrarlanamaz ama değerlere tekrar edebilir.
#*     Değiştirilebilir.
#*     Anahtar ile erişilir.

kisi = {"isim": "ali", "yas": 20, "cinsiyet": "m", "hobiler": ["Sinema", "Konser", "Yazılım"]}
# print(kisi["isim"])                              #*     Çıktı: ali


#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                           DEGER DEGISTIRME
#?----------------------------------------------------------------------------------------------------------------------------------------

# print(kisi)                                      #?     Çıktı: {'isim': 'ali', 'yas': 20, 'cinsiyet': 'm', 'hobiler': ['Sinema', 'Konser', 'Yazılım']}
# kisi["isim"] = "Ahmet"
# print(kisi)                                      #?     Çıktı: {'isim': 'Ahmet', 'yas': 20, 'cinsiyet': 'm', 'hobiler': ['Sinema', 'Konser', 'Yazılım']}



#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                    BIRDEN FAZLA DEGER DEGISTIRME
#TODO-------------------------------------------------------------------------------------------------------------------------------------

# print(kisi)                                      #TODO  Çıktı: {'isim': 'ali', 'yas': 20, 'cinsiyet': 'm', 'hobiler': ['Sinema', 'Konser', 'Yazılım']}
# kisi.update({"isim" : "Mehmet" , "yas" : 30})
# print(kisi)                                      #TODO  Çıktı: {'isim': 'Mehmet', 'yas': 30, 'cinsiyet': 'm', 'hobiler': ['Sinema', 'Konser', 'Yazılım']}

#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                          ANAHTAR DEGER EKLEME
#!----------------------------------------------------------------------------------------------------------------------------------------

# kisi["id"] = 12345
# print(kisi)

#!----------------------------------------------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                          ANAHTAR DEGER SILME
#*----------------------------------------------------------------------------------------------------------------------------------------

# print(kisi)                                      #*     Çıktı: {'isim': 'ali', 'yas': 20, 'cinsiyet': 'm', 'hobiler': ['Sinema', 'Konser', 'Yazılım'], 'id': 12345}
# del kisi["isim"]
# print(kisi)                                      #*     Çıktı: {'yas': 20, 'cinsiyet': 'm', 'hobiler': ['Sinema', 'Konser', 'Yazılım'], 'id': 12345}

#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                        FOR DONGUSU ILE YAZDIRMA
#?----------------------------------------------------------------------------------------------------------------------------------------

# for i in kisi:
#     print(i)                                     #?     Çıktı: Alt alta anahtarları yazar değerleri yazmaz.
# for j in kisi:
#     print(kisi[j])                               #?     Çıktı: Alt alta değerleri yazar anahtarları yazmaz. Bu aslında şu demek j = kişilerdeki anahtar. print(kisi[anahtar])

#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                       ANAHTARLARI SIRALAMA
#TODO-------------------------------------------------------------------------------------------------------------------------------------

# print(kisi.keys())                               #TODO  Çıktı: dict_keys(['isim', 'yas', 'cinsiyet', 'hobiler'])

#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                           DEGERLERI SIRALAMA
#!----------------------------------------------------------------------------------------------------------------------------------------

# print(kisi.values())                             #!     Çıktı: dict_values(['ali', 20, 'm', ['Sinema', 'Konser', 'Yazılım']])

#!----------------------------------------------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                      ANAHTAR VE DEGERLERI SIRALAMA
#*----------------------------------------------------------------------------------------------------------------------------------------

# print(kisi.items())                              #*     Çıktı: dict_items([('isim', 'ali'), ('yas', 20), ('cinsiyet', 'm'), ('hobiler', ['Sinema', 'Konser', 'Yazılım'])])
# print(kisi)                                      #*     Çıktı: {'isim': 'ali', 'yas': 20, 'cinsiyet': 'm', 'hobiler': ['Sinema', 'Konser', 'Yazılım']}

#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                        OLMAYAN ANAHTARI SORGULAMA
#?----------------------------------------------------------------------------------------------------------------------------------------

#?     Olmayan bir anahtarı yazdırırsan hata verir.
#?     print(kisi["id"])
print(kisi.get("id"))                            #?     Çıktı: None (Hata vermeden sorgulatır veya çalıştırır.)
print(kisi.get("isim","Bulunamadı"))             #?     Çıktı: ali  -->  "Bulunamadı" ilk parametre yoksa ekrana yazdıracağımız şey. Burada isim anahtarı var ama aşağıda id anahtarı olmaığı için "Bulunamadı" döndürdü.
print(kisi.get("id","Bulunamadı"))               #?     Çıktı: Bulunamadı  -->  "id" anahtarı olmadığı için ikinci parametredeki mesajımızı verdi.
#?----------------------------------------------------------------------------------------------------------------------------------------
