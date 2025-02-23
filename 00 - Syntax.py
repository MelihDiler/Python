# Yorum satırı "#" işareti ile yapılır.

# Kodlar satır bazlı çalışır ";" işaretini beklemez. 

# Satıra sığmadıysa ve kaydırma çubuğuyla gezinmemek için "\" işareti ile alt satırda koda devam edebilirsin. 
print \
("mfnkc")

# Aynı şekilde açık kalan "(", "[" ve "{" kapanmadıysa alt satırlara kadar devam eder.
a = (1 + 2 + 3 +
4 + 5 + 6 +
7 + 8 + 9) 
print (a)

# Aynı satırda birden fazla kodlama yapmak için ";" kullanılır.
a = 1; b = 2; c = 3;

# Anahtar kelimeler tanımlayıcı olarak kullanılamaz
# True, False, None haricinde tüm anahtar kelimeler küçük harfle başlar.
# Bir tanımlayıcı rakamla başlayamaz.
# Python büyük/küçük harfe duyarlı bir dildir. Bu, Değişken ve değişken tanımlayıcı isimlendirmelerinin aynı olmadığı anlamına gelmektedir.
# UTF-8 ile türkçe karakterleri destekleyecek hale gelebilir.
    
# Aşağıdaki örnekte görüldüğü gibi if'den sonra girinti ile ona ait bölüm başlar ve girintisiz ilk yer olan print (a) ile if dışına çıkılmış olur.
if b < 3:  
 print('Hello')
 a = 5 
print (a)


""" Bu bir
cok satirli
yorumdur. """

''' Bu da 
cok satirli
bir yorumdur. '''

def double(num):
 """double deger hesaplayan fonksiyon""" # Burada üç adet çift tırnakla yorum yerine doc. eklentisi yapmış olduk.
 return 2*num
print(double.__doc__)                    # Çünkü doc olarak çağırdık.

deger = 222 # deger değişkeni sayı (int) türünde
print(deger )
deger = "Anadolu" # deger değişkeni şimdi metin (string) türüne dönüştü
print(deger )

# Aynı zamanda birden çok değişkene, birden çok değer de atanabilir.
sayi1, sayi2, metin1 = 56, 11, "Eskisehir"

# Sabitlerin anlaşılabilmesi için hepsi büyük harfle ve aralarında "_" kullanılarak yapılmalı.
YER_CEKIMI = 9.80665
PI = 3.14159

# Python'da değişkenlere atanan değerlerin ya da dışarıdan kullanıcıdan alınan verilerin tipini öğrenebilmek için type() fonksiyonu kullanılmaktadır.
sayii = 2626
print(type(sayii ))  # Kod çıktısı <class 'int'>

# Tekli veya çoklu nesneyi silmek için "del" komutu kullanılabilir.
hiz = 50
mesafe = 60
del hiz, mesafe               
#print (hiz) "del hiz" komutu hiz değişkenini sildiği için print edilemiyor ve hata verdiği için yorum satırı yapıldı.

# Bir liste tanımlamak oldukça basittir. Virgülle ayrılmış öğeler parantez [ ] içine alınır.
listem = [34, 26.1, 'Python ogreniyorum']

# Tuple'ın listelerden farkı değişmez olmasıdır. Tuple'lar bir kez oluşturulduktan sonra değiştirilemez. 
# Tuple'lar, verileri yazmaya karşı korumak için kullanılır ve dinamik olarak değiştirilemedikleri için genellikle 
# listelerden daha hızlıdır. Tuple elemanları virgülle ayrılan parantez () içinde tanımlanır.
demet = ( 20.26, 'Anadolu', 26+4j )

sozluk = {1:'deger','anahtar':2.6}
print(type(sozluk ))                                          # <class 'dict'>
print("sozluk [1] = ", sozluk [1])                            # sozluk [1] = değer
print("sozluk ['anahtar'] = ", sozluk ['anahtar'])            # sozluk ['anahtar'] = 2.6                                          
# print("sozluk [2] = ", sozluk [2])                          # Hata oluşacaktır. çünkü 2 adında bir atama yoktur.

# Örtülü Tür Dönüşümü (Implicit)
sayi_int = 123
sayi_flo = 1.23
sayi_yeni = sayi_int + sayi_flo
print (sayi_yeni)                                             # Float veri tipindedir.

# Açık Tür Dönüşüm (Explicit)
sayi_int = 321
sayi_str = "987"
sayi_str = int(sayi_str)                                      # sayi_str artık int olmuştur. Artık toplama işlemi yapılabilir.

# çıkış işlemleri
print('Bu yazi ekrana yazdirilacak')
x = 925
print('x in degeri:', x)                                      # Burada metin ile x arasında kendiliğinden bir boşlukla geliyor. 
# print(*nesneler, sep=' ', end='\n', file=sys.stdout, flush=False) # Bu şekilde boşluk kapatılabilir yada araya başka ifadeler gelebilir.
print(1, 2, 3, 4)                                             # sep='' ile boşluk silinir
print(1, 2, 3, 4, sep='*')                                    # sep='*' ile boşluk yerine * gelir
print(1, 2, 3, 4, sep='|', end='&')                           # sep='|' ile boşluk yerine * gelir.


a = 13; b = 43
print('a degeri {} ve b degeri {}'.format(a,b))               # Kod çıktısı: a değeri 13 ve b değeri 43

# Virgülden sonra kaç hane yazılmasını istiyorsak .f arasına yazılmalı.
x = 123.456789
print('x degeri %.2f' %x)
print('x degeri %.4f' %x)

# Kullanıcıdan değer almak için:
veri = input('Bir sayi giriniz: ')
print( veri )
print( type( veri ) )
veri = int( veri )
print( type( veri ) )


