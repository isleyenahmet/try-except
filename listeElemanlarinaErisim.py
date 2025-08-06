def listeElemanlari(meyve):
    meyveler = {"elma": 15,
                 "armut":20 ,
                 "muz": 40,
                 "çilek": 100,
                 "kavun" : 90,
                 "karpuz": 35}
    for i in meyveler:
        if meyve not in meyveler:
            raise KeyError("Aranilan Meyve Listede Bulunmuyor!")
    print(f"{meyve} fiyati {meyveler[meyve]}")


meyve = input("Meyve Adini Girinzi: ")

try:
    listeElemanlari(meyve)
except KeyError as e:
    print(e)
