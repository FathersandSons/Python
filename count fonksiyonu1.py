##count listedeki ayni olan elemanlari sayar
liste=["a", "d", "p", "e", "ç", "a", "g"]
print(liste.count("a"))
for i in range(liste.count("a")):
    liste.remove("a")
print(liste)
