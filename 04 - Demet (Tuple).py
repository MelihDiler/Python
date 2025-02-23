
#*----------------------------------------------------------------------------------------------------------------------------------------
#*                                             DEMET (TUPLE)
#*----------------------------------------------------------------------------------------------------------------------------------------

#*     Değişmeyen verilerle çalışırken, sıralı ve sabit verilerin saklanması için tercih edilir.

#*     Değiştirilemez (Immutable): Bir tuple oluşturulduktan sonra içeriği değiştirilemez.
#*     Performans: Listelere göre daha hızlıdır çünkü sabit boyutludur.
#*     Kullanım Amacı: Veri güvenliğinin önemli olduğu yerlerde (örneğin, koordinatlar, sabit ayarlar).
#*     İndeksleme vardır.

bosDemet1 = ()
bosDemet2 = tuple()                              #*     Çıktı: Boş bir demeti demet nesnesi ile üretti. Üstteki ile aynı

demet = ("Sarı", "Mavi", "Yeşil", "Kırmızı", "Siyah")
print(type(demet))                               #*     Çıktı: <class 'tuple'>
print(len(demet))                                #*     Çıktı: 5  
print(demet[2])                                  #*     Çıktı: Yeşil

#*----------------------------------------------------------------------------------------------------------------------------------------
