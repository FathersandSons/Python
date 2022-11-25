adSoyad=input("lutfen adinizi ve soyadinizi giriniz...\t")
numara=input("lutfen okul numaranizi giriniz...\t")
sinav1=int(input("lutfen ilk sinavinizin sonucunu giriniz...\t"))
sinav2=int(input("lutfen ikinci sinavinizin sonucunu giriniz...\t"))
ortalama=((sinav1+sinav2)/2)
if ortalama<50:
    print(numara, "numarali sayin" ,adSoyad, "maalesef" ,ortalama, "ortalamayla sinifta kaldiniz.")
elif ortalama<70:
    print(numara, "numarali sayin" ,adSoyad, ortalama, "ortalamayla hicbir belge almadan duz gectiniz.")
elif ortalama<85:
    print(numara, "numarali sayin" ,adSoyad, ortalama, "ortalamayla tesekkur belgesi aldiniz.")
elif ortalama<100:
    print(numara, "numarali sayin" ,adSoyad, ortalama, "ortalamayla takdir belgesi aldiniz.")
elif ortalama==100:
    print(numara, "numarali sayin" ,adSoyad, ortalama, "ortalamayla onur belgesi aldiniz.")
else:
    print(numara, "numarali sayin" ,adSoyad, "yanlis giris yaptiniz.")
