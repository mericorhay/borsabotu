# borsabotu
Hisse senedi fiyat takipçisi
# Bu bir yatırım tavsiyesi değildir. Yalnızca fiyat hareketlerini izlemek için bir araçtır.
# Hisse Senedi Fiyat Takipçisi

Bu Python betiği, Google Finans'tan bir hisse senedinin fiyatını izler ve kullanıcı tanımlı parametrelere göre kar/zarar hesaplar.

## Kullanım

1. Depoyu yerel makinenize klonlayın veya indirin.
2. Gerekli kütüphaneleri pip kullanarak yükleyin:
pip install requests
pip install beautifulsoup4
pip install keyboard
3. Betiği çalıştırın:
4. İlgilendiğiniz hisse senedinin Google Finans URL'sini girin, kontrol aralığını ve lot maliyetini belirtin.
5. Program, fiyatı belirli aralıklarla izleyecek ve kar/zarar durumunu hesaplayacaktır.
7. Eğer Borsa İstanbul haricinde diğer hisselerle işlem yapılacaksa  fiyat = fiyat[1:-3] (kod satırı line 28)  ,  fiyat[:-3] Olarak değiştirilmelidir


## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LİSANS]) dosyasına bakın.
