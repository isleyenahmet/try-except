def parolaKontrol(parola):
    turkce_karakterler = "şçıöğü"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parolanizda Turkce karakterler bulunuyor")
    print("Gecerli Parola")

parola = input("Parola: ")

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)
    
