okul=input("lutfen internet sitesini  giriniz...\t")
if okul.startswith("www.") or okul.startswith("https://www."):
    if okul.endswith("meb.k12.tr"):
        print("siteniz okul sitesidir")
    else:
        print("siteniz okul sitesi degildir")
else:
    print("hatali giris")
