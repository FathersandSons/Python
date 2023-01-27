print ("""bu bir dort islem programidir.
toplama icin + 'ya
cikarma icin - 'ye
carpma icin * 'ya
bolma icin / 'ye basiniz""")
islem=input("islem secimi icin operator seciniz...\t")
if islem=="+":
    toplam=0
    while True:
        sayi=float(input("lutfen bir sayi giriniz, bitirmek icin 0'a basiniz...\t"))
        if sayi!=0:
                toplam=toplam+sayi
        else:
            break
    print(toplam) 
elif islem=="-":
    fark=0
    while True:
        sayi=float(input("lutfen bir sayi giriniz, bitirmek icin 0'a basiniz...\t"))
        if sayi!=0:
                fark=sayi-fark
        else:
            break
    print(fark)
elif islem=="*":
    carpim=1
    while True:
        sayi=float(input("lutfen bir sayi giriniz, bitirmek icin 1'e basiniz...\t"))
        if sayi!=1:
            carpim=carpim*sayi
        else:
            break
    print(carpim)
elif islem=="/":
    bolum=float(input("lutfen bolunen sayiyi giriniz...\t"))
    while True:
        sayi=float(input("lutfen bolen sayiyi giriniz, bitirmek icin 1'e basiniz...\t"))
        if sayi==0:
            print("cevap tanimsizdir...")
            break
        else:
            if sayi!=1:
                bolum=bolum/sayi
            else:
                print(bolum)
                break
else:
    print("hatali giris yaptiniz...")
