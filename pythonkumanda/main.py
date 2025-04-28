import random
import time

class Kumanda():
    def __init__(self, tv_durum="Açık", ses=0, kanal="trt", kanal_listesi=None, parlaklık=0, izleme_modu="Seçilmedi", zoom=1):
        if kanal_listesi is None:
            kanal_listesi = ["star", "atv", "trt", "show"]
        self.tv_durum = tv_durum
        self.ses = ses
        self.kanal = kanal
        self.kanal_listesi = kanal_listesi
        self.parlaklık = parlaklık
        self.izleme_modu = izleme_modu
        self.zoom = zoom

    def tv_ayrıntılar(self):
        print(f""" 
Televizyon Durumu: {self.tv_durum}
Ses Düzeyi: {self.ses}
Şu Anki Kanal: {self.kanal}
Kanal Listesi: {self.kanal_listesi}
Parlaklık: {self.parlaklık}
İzleme Modu: {self.izleme_modu}
Zoom Oranı: {self.zoom}x
        """)

    def tv_aç(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık!")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapa(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı!")
        else:
            print("Televizyon kapatılıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayar(self):
        while True:
            giriş = input("Ses artırmak için '>' azaltmak için '<' tuşlayın, çıkmak için başka tuşa basın: ")
            if giriş == ">":
                if self.ses < 31:
                    self.ses += 1
                    print("Ses:", self.ses)
            elif giriş == "<":
                if self.ses > 0:
                    self.ses -= 1
                    print("Ses:", self.ses)
            else:
                print("Ses ayarı güncellendi:", self.ses)
                break

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:", self.kanal)

    def kanal_ekle(self, yeni_kanal):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(yeni_kanal)
        print("Kanal eklendi:", yeni_kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return f"Televizyon Durumu: {self.tv_durum}\nSes: {self.ses}\nKanal: {self.kanal}\nKanal Listesi: {self.kanal_listesi}\nParlaklık: {self.parlaklık}\nİzleme Modu: {self.izleme_modu}\nZoom: {self.zoom}x"

    def parlaklık_ayarı(self):
        while True:
            seçim = input("Parlaklık artırmak için '+' azaltmak için '-' basın, çıkmak için başka bir tuş: ")
            if seçim == "+":
                if self.parlaklık < 50:
                    self.parlaklık += 2
                    print("Parlaklık:", self.parlaklık)
            elif seçim == "-":
                if self.parlaklık > 0:
                    self.parlaklık -= 2
                    print("Parlaklık:", self.parlaklık)
            else:
                print("Güncel parlaklık:", self.parlaklık)
                break

    def mod_değiştir(self):
        modlar = ["Genel", "Sinema", "Spor", "Haber", "Nostaljik", "Modern", "Belgesel"]
        i = 0
        while True:
            mod_seç = input("Mod değiştirmek için 'm' tuşlayın, çıkmak için başka bir tuş: ")
            if mod_seç == "m":
                self.izleme_modu = modlar[i]
                print("İzleme Modu:", self.izleme_modu)
                i += 1
                if i == len(modlar):
                    i = 0
            else:
                print("Mod seçiminden çıkılıyor...")
                break

    def zoom_ayarı(self):
        while True:
            kullanıcı = input("Zoom artırmak için '+', azaltmak için '-', çıkmak için başka bir tuş: ")
            if kullanıcı == "+":
                if self.zoom < 16:
                    self.zoom *= 2
                    print("Güncel Zoom Oranı:", int(self.zoom))
            elif kullanıcı == "-":
                if self.zoom > 1:
                    self.zoom /= 2
                    print("Güncel Zoom Oranı:", int(self.zoom))
            else:
                print("Zoom ayarlarından çıkılıyor...")
                break

    def yer_değiştir(self):
        while True:
            indis = input("Değiştirmek istediğiniz iki kanal indisini araya ',' koyarak girin (örn: 1,2) veya çıkmak için 'q' tuşlayın: ")
            if indis == "q":
                print("Yer değiştiriciden çıkılıyor...")
                break
            try:
                i1, i2 = map(int, indis.split(","))
                self.kanal_listesi[i1], self.kanal_listesi[i2] = self.kanal_listesi[i2], self.kanal_listesi[i1]
                print("Güncellenmiş kanal listesi:", self.kanal_listesi)
            except:
                print("Hatalı giriş yaptınız!")

# Ana Program
kumanda = Kumanda()

print("""
Televizyon Kumandası Programına Hoşgeldiniz
1- Tv Aç
2- Tv Kapat
3- Ses Ayarları
4- Kanal Ekle
5- Kanal Sayısını Öğren
6- Rastgele Kanal Değiştir
7- Tv Bilgileri
8- Kanal Yerlerini Değiştir
9- Parlaklık Ayarı
10- İzleme Modu Seçimi
11- Zoom Ayarı
Çıkış için 'q' tuşlayın
""")

while True:
    işlem = input("İşlemi seçiniz: ")
    if işlem == "q":
        print("Programdan çıkılıyor...")
        break
    elif işlem == "1":
        kumanda.tv_aç()
    elif işlem == "2":
        kumanda.tv_kapa()
    elif işlem == "3":
        kumanda.ses_ayar()
    elif işlem == "4":
        yeni_kanallar = input("Eklemek istediğiniz kanalları ',' ile ayırarak giriniz: ")
        for kanal in yeni_kanallar.split(","):
            kumanda.kanal_ekle(kanal.strip())
    elif işlem == "5":
        print("Toplam Kanal Sayısı:", len(kumanda))
    elif işlem == "6":
        kumanda.rastgele_kanal()
    elif işlem == "7":
        print(kumanda)
    elif işlem == "8":
        kumanda.yer_değiştir()
    elif işlem == "9":
        kumanda.parlaklık_ayarı()
    elif işlem == "10":
        kumanda.mod_değiştir()
    elif işlem == "11":
        kumanda.zoom_ayarı()
    else:
        print("Geçersiz işlem!")
