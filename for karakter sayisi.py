metin=input("lutfen bir metin giriniz...\t")
i=0
j=0
for karakter in metin:
    i=i+1
    if karakter==" ":
        j=j+1
    m=i-j
    k=j+1
print("""girdiginiz metnin toplam karakter sayisi {},
bosluksuz karakter sayisi {},
bosluk sayisi {},
kelime sayisi ise {}'dir.""".format(i,m,j,k))
