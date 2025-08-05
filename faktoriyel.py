#Faktöritel Uygulamasi
def faktoriyel(x):
    x = int(x)

    if(x < 0):
        raise ValueError("Negatif Sayilarin faktoriyeli hesaplanamaz!")
    sonuc = 1

    for i in range(1, x+1):
        sonuc *= i

    return sonuc

for i in [3,5,"2a",-7,-9,45]:
    try:
        x = faktoriyel(i)
    except ValueError as e: #bir valueError oluşursa bunu e de tut ve ekrana yazır aslında if altındaki valueErroru tutacak
        print(e)
        continue
    else:
        print(x)

        



