##extend bir listeyi diger listeye eklemek
liste=["a", "d", "p", "e", "t", "a"]
bilgi=[1, 2, 3, 4, 5]
liste.extend(bilgi)
print(liste)
liste[2]=bilgi
print(liste)
