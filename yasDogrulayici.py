#Girilen Yaş 0 dan küçükse uyarı ver
def yasDogrulayici(yas):
    if yas < 0:
        raise ValueError("Yas Degeri 0 dan Küçük olamaz!")
    print(f"Girilen Yas {yas}")

yas = int(input("Yasinizi Giriniz: "))

try:
    yasDogrulayici(yas)
except ValueError as e:
    print(e)