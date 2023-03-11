def Hesapla(taban,us):
    sonuc=taban**us
    son=int(input("sondan kac karakterin yazilmasini istiyorsunuz...\t"))
    print(sonuc)
    print(str(sonuc)[-son:])    
x=int(input("lutfen taban degerini giriniz...\t"))
y=int(input("lutfen us degerini giriniz...\t"))
Hesapla(x,y)
