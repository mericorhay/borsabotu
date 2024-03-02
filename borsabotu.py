#Kütüphaneler
from smtplib import SMTP
import requests
from bs4 import BeautifulSoup
import time
#BULUTTA ÇALIŞACAĞI İÇİN KEYBOARD KÜTÜPHANESİ VE ÇIKMA FONKSİYONU EKLENMEDİ
#URLSETTİNGS
#FONKSİYONLAR


def mailto(sonkar_zarar):
    try:
        baslik = "Borsa Bilgilendirme Mesajınız"
        mesaj = None
        # Hesaplama yapılacak değer
        if sonkar_zarar >= int(karlılık):
            mesaj = f"Sistem Kendini Uykuya aliyor (20 Dakika) {sonkar_zarar} TL Kadar Kar Ettiniz"
            if mesaj is not None:
                content = "Subject:{0}\n\n{1}".format(baslik, mesaj)

                mailiniz = "*********"
                sifreniz = "*********"
                gidecek = "***********" #Gİdecek Kişinin Maili

                outlook = SMTP("smtp-mail.outlook.com", 587)
                outlook.starttls()
                outlook.login(mailiniz, sifreniz)
                outlook.sendmail(mailiniz, gidecek, content.encode("utf-8"))

                print("Mail Gönderme İşlemi Başarılı")
            time.sleep(1200)

        elif sonkar_zarar <= int(abs(karlılık)):
            mesaj = f"Sistem Kendini Uykuya aliyor (20 Dakika) {sonkar_zarar} TL Kadar Zarar Ettiniz"
            if mesaj is not None:
                content = "Subject:{0}\n\n{1}".format(baslik, mesaj)

                mailiniz = "mericorhayy@gmail.com"
                sifreniz = "4680215m"
                gidecek = "zoramagercek@gmail.com"

                outlook = SMTP("smtp-mail.outlook.com", 587)
                outlook.starttls()
                outlook.login(mailiniz, sifreniz)
                outlook.sendmail(mailiniz, gidecek, content.encode("utf-8"))

                print("Mail Gönderme İşlemi Başarılı")
            time.sleep(1200)


    except Exception as e:
        print("Mail Gönderilemedi")
        print(e)



def karzarar():
    alis_maliyeti = lotmaliyet * lotsayisi
    satis_geliri = yeni_son_fiyat * lotsayisi
    kar_zarar = yeni_son_fiyat - lotmaliyet
    sonkar_zarar = kar_zarar*lotsayisi
    print("Anlık Kar/Zarar",sonkar_zarar)
    return sonkar_zarar
#FONKSİYONLAR BİTİŞ
karlılık = input("Kaç TL kazandığınızda Otomaik Olarak Mail Gönderilsin")
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


    if yeni_son_fiyat > son_fiyat:
        karzarar()
        print("Fiyat Yükseldi")
        print(f"Yeni Fiyat {yeni_son_fiyat}")
        print("Eski Fiyat", son_fiyat)
        print("Fark", yeni_son_fiyat - son_fiyat)
        print("*" * 50)
        sonkar_zarar = karzarar()
        mailto(sonkar_zarar)

    elif yeni_son_fiyat == son_fiyat:
        karzarar()
        print("Herhangi bir değişiklik yok")
        print("Yeni Fiyat", yeni_son_fiyat)
        print("Eski Fiyat", son_fiyat)
        print("*"*50)
        sonkar_zarar = karzarar()
        mailto(sonkar_zarar)

    else:
        karzarar()
        print("Fiyat Düştü")
        print("Fark", son_fiyat - yeni_son_fiyat)
        print(yeni_son_fiyat)
        print("*" * 50)
        sonkar_zarar = karzarar()
        mailto(sonkar_zarar)
