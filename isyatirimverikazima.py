import requests
from bs4 import BeautifulSoup
import time
import re

class Hisse:
    def __init__(self):
        self.dongu=True

    def program(self):
        secim=self.menu()
        if secim=="1":
            print("Guncel fiyatlar aliniyor...\n")
            time.sleep(3)
            self.guncelfiyat()
        if secim=="2":
            print("Kunye bilgileri aliniyor...\n")
            time.sleep(3)
            self.kunye()
        if secim=="3":
            print("Cari degerler aliniyor...\n")
            time.sleep(3)
            self.carideger()
        if secim=="4":
            print("Getiri bilgileri aliniyor...\n")
            time.sleep(3)
            self.getiri()
        if secim=="5":
            print("Endeks oranlari aliniyor...\n")
            time.sleep(3)
            self.dahilendeks()
        if secim=="6":
            print("Cikis yapiliyor...\n")
            time.sleep(3)
            self.cikis()
        
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-6]",secim):
                raise Exception("Lutfen 1 ve 6 arasinda bir secim yapiniz")
            elif len(secim)!=1:
                raise Exception("Lutfen 1 ve 6 arasinda bir secim yapiniz")
        while True:
            try:
                secim=input("Merhabalar, Ekonomi Sitemize Hosgeldiniz...\n Lutfen Bir secim Yapiniz...\n[1]-Guncel Fiyat Bilgisi Alma...\n[2]-Kunye Bilgileri Alma...\n[3]-Cari Degerleri Alma...\n[4]-Getiri Bilgileri Alma...\n[5]-Endeks Oranlari Alma...\n[6]-Sistemden Cikis...")
                kontrol(secim)
                break
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim
    def guncelfiyat(self):
        while True:
            try:
                sirket=input("Lutfen Sirket Adi Giriniz..\n")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx"
                
                baglan=requests.get(url)
                kod=baglan.content
                parser=BeautifulSoup(kod,"html.parser")
                fiyat=parser.find("a",{"href":"/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)})\
                .parent.parent.find_all("td")
                bilgi1=fiyat[1].string
                bilgi2=fiyat[2].span.string
                bilgi3=fiyat[3].string
                bilgi4=fiyat[4].string
                bilgi5=fiyat[5].string
                print(f"Son Fiyat:{bilgi1}\n Degisim(%):{bilgi2.lstrip()}\r Degisim(TL):{bilgi3}\n Hacim(TL):{bilgi4}\n Hacim(Adet):{bilgi5}")
                break
            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
            time.sleep(3)
        self.menudon()

    def kunye(self):
        while True:
            try:
                sirket=input("Lutfen Sirket Adi Giriniz..\n")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                
                baglan=requests.get(url)
                kod=baglan.content
                parser=BeautifulSoup(kod,"html.parser")
                kunye=parser.find("div",{"id":"ctl00_ctl58_g_6618a196_7edb_4964_a018_a88cc6875488"}).find_all("tr")
                kunye1=kunye[0].find("td").string
                kunye2=kunye[1].find("td").string
                kunye3=kunye[2].find("td").string
                kunye4=kunye[3].find("td").string
                kunye5=kunye[4].find("td").string
                kunye6=kunye[5].find("td").string
                print(f"Unvan:{kunye1}\nKurulus:{kunye2}\nFaal Alani:{kunye3}\nTelefon:{kunye4}\nFaks:{kunye5}\nAdres:{kunye6}")
                break
            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
            time.sleep(3)
        self.menudon()
    def carideger(self):
        while True:
            try:
                sirket=input("Lutfen Sirket Adi Giriniz..\n")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                
                baglan=requests.get(url)
                kod=baglan.content
                parser=BeautifulSoup(kod,"html.parser")
                cari=parser.find("div",{"id":"ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"}).find_all("tr")
                for i in cari:
                    bilgi1=i.th.string
                    bilgi2=i.td.string
                    print(f"{bilgi1}:{bilgi2}")
                break
            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
            time.sleep(3)
        self.menudon()
    def getiri(self):
        while True:
            try:
                sirket=input("Lutfen Sirket Adi Giriniz..\n")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                
                baglan=requests.get(url)
                kod=baglan.content
                parser=BeautifulSoup(kod,"html.parser")
                getiri=parser.find("div",{"id":"ctl00_ctl58_g_aa8fd74f_f3b0_41b2_9767_ea6f3a837982"}).find("table")\
                .find("tbody").find_all("tr")
                for i in getiri:
                    bilgi1=i.find_all("td")
                    print(f"Birim:{bilgi1[0].string}\nBir Gün içerisindeki getiri(%):{bilgi1[1].string}\nBir hafta içerisindeki(%):{bilgi1[2].string}\nBir ay içerisindeki(%):{bilgi1[3].string}\nYıl içi getiri:{bilgi1[4].string}")
                break
            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
            time.sleep(3)
        self.menudon()
    def dahilendeks(self):
        while True:
            try:
                sirket=input("Lutfen Sirket Adi Giriniz..\n")
                url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                
                baglan=requests.get(url)
                kod=baglan.content
                parser=BeautifulSoup(kod,"html.parser")
                dahiliendeks=parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}).find("table").find("thead").find("tr").find_all("th")
                dahiliendeks2=parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}).find("table").find("tbody").find("tr").find_all("td")
                for i in range(0,3):
                    print(f"{dahiliendeks[i].string}:{dahiliendeks2[i].string}")
                break
            except AttributeError:
                print("Hatali bir sirket adi girdiniz")
                time.sleep(3)
            time.sleep(3)
        self.menudon()
    def cikis(self):
        self.dongu=False
        exit()

    def menudon(self):
        while True:
            x=input("Ana menuye donmek icin 7'ye, Cikmak icin lutfen 6'ya basiniz")
            if x=="7":
                print("Ana menuye donuluyor")
                time.sleep(3)
                self.program()
            elif x=="6":
                print("Sistemden cikis yapiliyor")
                time.sleep(3)
                self.cikis()
            else:
                print("Lutfen gecerli bir secim yapiniz")

sistem=Hisse()

while sistem.dongu:
    sistem.program()


