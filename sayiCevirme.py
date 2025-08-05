try:
    sayi = int(input("Bir Sayi Giriniz:"))
    sonuc = 10/sayi
    print(f"Sayinin 10 a bölümünden kalan: {sonuc}")
except ValueError:
    print("Lutfen Bir Tam Sayi Giriniz! ")
except ZeroDivisionError:
    print("Sifira bolme hatasi!")