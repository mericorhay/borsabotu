#Kütüphaneler
import sys
import keyboard
import requests
from bs4 import BeautifulSoup
import time
#URLSETTİNGS
#FONKSİYONLAR
def karzarar():
    alis_maliyeti = lotmaliyet * lotsayisi
    satis_geliri = yeni_son_fiyat * lotsayisi
    kar_zarar = yeni_son_fiyat - lotmaliyet
    sonkar_zarar = kar_zarar*lotsayisi
    print("Anlık Kar/Zarar",sonkar_zarar)
    return sonkar_zarar
#FONKSİYONLAR BİTİŞ

url = input("Lütfen bir Google Financeda ilgilendiğiniz hissenin URL sini giriniz: ")
zaman = float(input("Kaç Saniye Sonra Veriyi Karşılaştıracağını Giriniz (Saniye Cinsinden)"))
lotmaliyet = int(input("Lot Maliyetinizi Giriniz"))
lotsayisi = int(input("Lot Sayınızı Girin"))
print("Programdan Çıkmak için Tuşunuz (Q)")
#Döngü Başlangıç
while True:
    fiyaturl = requests.get(url)
    soup = BeautifulSoup(fiyaturl.content, "html.parser")
    fiyat = soup.find("div", class_="YMlKec fxKbKc").text
    fiyat = fiyat[1:-3] #ÇOK ÖNEMLİ GELEN VERİ STRİNGTEN DÖNÜŞÜM YAPILAMADIĞI İÇİN SİSTEM TARAFINDAN OTO YAPILIYOR

    fiyatrp = fiyat.replace(" ", "").strip()
    #FLOAT VERİ TİPİNE DÖNÜŞÜM
    try:
        son_fiyat = int(fiyatrp)
    except ValueError:
        print("Hata: Fiyat verisi uygun formatta değil.")
        continue
    #ESKİ VERİ İLE YENİ VERİ ARASINDAKİ FARK
    time.sleep(zaman)

    fiyaturlnew = requests.get(url)
    corba = BeautifulSoup(fiyaturlnew.content, "html.parser")
    yeni_fiyat = corba.find("div", class_="YMlKec fxKbKc").text #GOOGLE FİNANCE DEĞİŞİKLİK OLURSA DEĞİŞTİRİLECEK*
    yeni_fiyat = yeni_fiyat[1:-3]

    yeni_fiyatrp = yeni_fiyat.replace(" ", "").strip()
    #Çok Önemli Float veri Tipine dönüşüm
    try:
        yeni_son_fiyat = int(yeni_fiyatrp)
    except ValueError:
        print("Hata: Yeni fiyat verisi uygun formatta değil.")
        continue

    if keyboard.is_pressed('q'):
        print("Program sonlandırılıyor...")
        sys.exit()
    if yeni_son_fiyat > son_fiyat:
        karzarar()
        print("Fiyat Yükseldi")
        print(f"Yeni Fiyat {yeni_son_fiyat}")
        print("Eski Fiyat", son_fiyat)
        print("Fark", yeni_son_fiyat - son_fiyat)
        print("*" * 50)

    elif yeni_son_fiyat == son_fiyat:
        karzarar()
        print("Herhangi bir değişiklik yok")
        print("Yeni Fiyat", yeni_son_fiyat)
        print("Eski Fiyat", son_fiyat)
        print("*"*50)

    else:
        karzarar()
        print("Fiyat Düştü")
        print("Fark", son_fiyat - yeni_son_fiyat)
        print(yeni_son_fiyat)
        print("*" * 50)
# Bu bir yatırım tavsiyesi değildir. Yalnızca fiyat hareketlerini izlemek için bir araçtır.
        #MIT License

#Copyright (c) 2024 mericorhay

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
##copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

##copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


#MIT License

#Telif Hakkı © 2024 [mericorhay]

#Bu yazılım ve belgelendirme dosyaları ("Yazılım"), kullanım, kopyalama, değiştirme, birleştirme, yayımlama, dağıtma, alt lisanslama ve/veya satma hakkına sahip olan herkese verilmiştir, yazılımın kopyalarını sunan ve aşağıdaki koşulların altında:

#YAZILIM "OLDUĞU GİBİ" SAĞLANIR, HERHANGİ BİR GARANTİ VERİLMEMEKTEDİR, SATILABİLİRLİK, BELİRLİ BİR AMACA UYGUNLUK VEYA İHLAL DURUMU DAHİL OLMAK ÜZERE AÇIK VEYA ZIMNİ HER TÜRLÜ GARANTİLER DAHİL OLMAK ÜZERE, ANCAK BUNLARLA SINIRLI VE BU YAZILIM İLE İLGİLİ RİSKLERİN SİZİN SORUMLULUĞUNUZDA OLDUĞUNU KABUL EDER. HERHANGİ BİR KOŞULDA, YAZARLAR VEYA TELİF HAKKI SAHİPLERİ HERHANGİ BİR TALEP, ZARAR VEYA DİĞER SORUMLULUKTAN SORUMLU DEĞİLDİR, YAZILIMLA VEYA YAZILIMIN KULLANIMI VEYA BAŞKA YAZILIMLARLA İLGİLİ.


