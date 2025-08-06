try:
    a = int(input("1. Sayiyi Giriniz: "))
    b = int(input("2. Sayiyi Giriniz: "))
    print("Carpimlari: ", a*b)
except ValueError:
    print("Girilen İki İfadenin De Sayi Olduğundan Emin Olunuz!!")