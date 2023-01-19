def Toplama(x,y):
    sonuc=x+y
    print("girdiginiz iki sayinin toplami:", sonuc)
def Cikarma(x,y):
    sonuc1=x-y
    print("girdiginiz iki sayinin farki:",sonuc1)
def Carpma(x,y):
    sonuc2=x*y
    print("girdiginiz iki saniyinin carpimi:",sonuc2)
def Bolme(x,y):
    sonuc3=x/y
    print("girdiginiz iki sayinin birbirine bolumu:",sonuc3)
secim=input("""
Islem turu : + Toplama
             - Cikarma
             * Carpma
             / Bolme\t""")
if secim=="+":
    s1=int(input("lutfen bir sayi giriniz...\t"))
    s2=int(input("lutfen bir sayi daha giriniz...\t"))
    Toplama(s1,s2)
elif secim=="-":
    s1=int(input("lutfen bir sayi giriniz...\t"))
    s2=int(input("lutfen bir sayi daha giriniz...\t"))
    Cikarma(s1,s2)
elif secim=="*":
    s1=int(input("lutfen bir sayi giriniz...\t"))
    s2=int(input("lutfen bir sayi daha giriniz...\t"))
    Carpma(s1,s2)
elif secim=="/":
    s1=int(input("lutfen bir sayi giriniz...\t"))
    s2=int(input("lutfen bir sayi daha giriniz...\t"))
    Bolme(s1,s2)
else:
    print("hatali giris yaptiniz...")
