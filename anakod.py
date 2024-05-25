import random

# karakterler
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# uzunluk
parola_uzunlugu = int(input("Parolanın uzunluğu kaç olmasını istersiniz?: "))

# şifre
parola1 = ""

#random
for i in range(parola_uzunlugu):
    rastgele_karakter = random.choice(karakterler)
    parola1 = parola1 + rastgele_karakter

# konsola yazdırma
print("Parolanız:", parola1)
