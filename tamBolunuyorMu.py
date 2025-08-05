def tamBolunuyorMu(sayi):
    if sayi%5 != 0:
        raise ValueError("Sayiniz 5'e Bolunmuyor")
    print("Sayi Tam Bölünür")

sayi = int(input("Sayi Giriniz: "))

try: #denemeye çalış
    tamBolunuyorMu(sayi)
except ValueError as e: #hata olursa yakala
    print(e)
        