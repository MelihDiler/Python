

#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                               LISTELER                                   
#*----------------------------------------------------------------------------------------------------------------------------------------

#*     Sıralı ve değiştirilebilir verilerle çalışırken, öğelere indeksleme ile erişim gerektiğinde kullanılır.

bosListe1= []
bosListe2 = list()                               #*     Çıktı: Boş bir listeyi list nesnesi ile üretti. Üstteki ile aynı

renkler = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
# print(type(renkler))                             #*     Çıktı: <class 'list'>
# print(len(renkler))                              #*     Çıktı: 5
# print(renkler[1])                                #*     Çıktı: Beyaz
# #*print(renkler[6])                              #*     6. indeks olmadığı için hata vericek.
# print(renkler[2:])                               #*     Çıktı: ['Sarı', 'Mavi', 'Yeşil']
# print(renkler[1:4])                              #*     Çıktı: ['Beyaz', 'Sarı', 'Mavi']
# print(renkler[:4])                               #*     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi']
# print(renkler[::2])                              #*     Çıktı: ['Siyah', 'Sarı', 'Yeşil']          -->  ilk parametre boş olduğu için baştan başladı. İkinci parametrede boş olduğu için sonuna kadar gidecek. Üçüncü parametrede 2 olduğu için ikişer ikişer ilerleyecek.

#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                                APPEND
#?----------------------------------------------------------------------------------------------------------------------------------------

#?     Listenin sonuna eleman ekler

# print(renkler)                                   #?     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# renkler.append("Gri")
# print(renkler)                                   #?     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil', 'Gri']



#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                              INSERT
#TODO-------------------------------------------------------------------------------------------------------------------------------------

#TODO  Belirlediğimiz indekse eleman ekler

# print(renkler)                                   #TODO  Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# renkler.insert(0,"Gri")
# print(renkler)                                   #TODO  Çıktı: ['Gri', 'Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']

#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                                 EXTENT
#!----------------------------------------------------------------------------------------------------------------------------------------

#!     Birden fazla değer ekler
# renkler2 = ["Turuncu", "Pembe"]

# print(renkler)                                   #!     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# renkler.extend(renkler2)
# print(renkler)                                   #!     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil', 'Turuncu', 'Pembe']

#!     Eğer ki bu append ile yapsaydık çıktımıız liste içinde liste olucaktı  -->  ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil', ['Turuncu', 'Pembe']]

#!----------------------------------------------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                                 REMOVE
#*----------------------------------------------------------------------------------------------------------------------------------------

#*     Belirlediğimiz elemanı siler

# print(renkler)                                   #*     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# renkler.remove("Sarı")
# print(renkler)                                   #*     Çıktı: ['Siyah', 'Beyaz', 'Mavi', 'Yeşil']

#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                                   POP   
#?----------------------------------------------------------------------------------------------------------------------------------------

#?     Listenin en son elemanın silip geri döndürür.

# print(renkler)                                   #?     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# silinen = renkler.pop()
# print(renkler)                                   #?     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi']
# print(silinen)                                   #?     Çıktı: Yeşil


#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                              REVERSE                                   
#TODO-------------------------------------------------------------------------------------------------------------------------------------

#TODO  Listeyi tersine çevirir. Eski liste değişir.

# print(renkler)                                   #TODO  Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# renkler.reverse()
# print(renkler)                                   #TODO  Çıktı: ['Yeşil', 'Mavi', 'Sarı', 'Beyaz', 'Siyah']


#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                                   SORT
#!----------------------------------------------------------------------------------------------------------------------------------------

#!     Listeyi alfabetik sıralar. Eski liste deişir.

# print(renkler)                                   #!     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# renkler.sort()
# print(renkler)                                   #!     Çıktı: ['Beyaz', 'Mavi', 'Sarı', 'Siyah', 'Yeşil']

#!     Tersten sıralama:

# renkler.sort(reverse = True)
# print(renkler)                                   #!     Çıktı: ['Yeşil', 'Siyah', 'Sarı', 'Mavi', 'Beyaz']

#!----------------------------------------------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                                 SORTED
#*----------------------------------------------------------------------------------------------------------------------------------------

#*     Listeyi alfabetik sıralayıp değişkene atar. Eski liste değişmez

# print(renkler)                                   #*     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# yeniListe = sorted(renkler)                      
# print(renkler)                                   #*     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']
# print(yeniListe)                                 #*     Çıktı: ['Beyaz', 'Mavi', 'Sarı', 'Siyah', 'Yeşil']

#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                                  MIN
#?----------------------------------------------------------------------------------------------------------------------------------------

#?     Stringlerde alfabetik olarak en küçüğü sayısal değerlerde de yine en düşüğü döndürür.

sayilar = [1,2,3,4,5,6,7,8]

# print(min(renkler))                              #?     Çıktı: Beyaz
# print(min(sayilar))                              #?     Çıktı: 1

#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                               MAX
#TODO-------------------------------------------------------------------------------------------------------------------------------------

#TODO  Stringlerde alfabetik olarak en büyüğü sayısal değerlerde de yine en büyüğü döndürür.

# print(max(renkler))                              #?     Çıktı: Yeşil
# print(max(sayilar))                              #?     Çıktı: 8


#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                                  IN
#!----------------------------------------------------------------------------------------------------------------------------------------

#!     Listede var mı yok mu kontrolü

# print(3 in sayilar)                              #!     Çıktı: True

#!----------------------------------------------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                                  SUM
#*----------------------------------------------------------------------------------------------------------------------------------------

#*     Listedeki sayıların toplamını döndürür. Stringlerde hata alırsın.

# print(sum(sayilar))                              #?     Çıktı: 36


#*----------------------------------------------------------------------------------------------------------------------------------------
#?----------------------------------------------------------------------------------------------------------------------------------------
#?                                         FOR ILE LISTEYI YAZDIRMA
#?----------------------------------------------------------------------------------------------------------------------------------------

#?     for ile renkler listesinde tek tek değerleri renk değişkenine dön, print ile yazdır.

# for renk in renkler:                             #?     Çıktı: Alt alta Siyah, Beyaz, Sarı, Mavi, Yeşil
#     print(renk)

#?----------------------------------------------------------------------------------------------------------------------------------------
#TODO-------------------------------------------------------------------------------------------------------------------------------------
#TODO                                            ENUMERATE
#TODO-------------------------------------------------------------------------------------------------------------------------------------

#TODO  Listemizi numaralandırarak sıralar. start ile kaçtan başlayacağını belirleyebiliriz. Yazmazsak sıfırdan başlar.

# print(list(enumerate(renkler,start=3)))          #TODO  Çıktı: [(3, 'Siyah'), (4, 'Beyaz'), (5, 'Sarı'), (6, 'Mavi'), (7, 'Yeşil')]


#TODO-------------------------------------------------------------------------------------------------------------------------------------
#!----------------------------------------------------------------------------------------------------------------------------------------
#!                                        LISTEYI STRINGE CEVIRME    
#!----------------------------------------------------------------------------------------------------------------------------------------

#!     join metotu ile listeyi stringe çeviririz. "" arasına ne yazarsan onu her değerin arasına koyar. Boşluk koyabilirsin veya virgül.

# stringRenkler = "*".join(renkler)
# print(stringRenkler)                             #!     Çıktı: Siyah*Beyaz*Sarı*Mavi*Yeşil

#!----------------------------------------------------------------------------------------------------------------------------------------
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                        STRINGI LISTEYE CEVIRME
#*----------------------------------------------------------------------------------------------------------------------------------------

#*     split metotu ile stringi listeye çeviririz. "" arasına ne koyarsan her onu gördüğünde bölerek listeye bir değer olarak ekler.

# listeyeCevir = stringRenkler.split("*")
# print(listeyeCevir)                              #*     Çıktı: ['Siyah', 'Beyaz', 'Sarı', 'Mavi', 'Yeşil']


#*----------------------------------------------------------------------------------------------------------------------------------------


