adSoyad=(input("lutfen adinizi soyadinizi girin...\t"))
kullaniciAdi=(input("lutfen kullanici adinizi girin...\t"))
sifre=(input("lutfen bir sifre girin...\t"))
if kullaniciAdi=="admin" and sifre=="1234":
    print("sayin",adSoyad,"hesabiniza giris yaptiniz")
else:
    print("sayin",adSoyad,"hesabiniza giris yapamadiniz")
