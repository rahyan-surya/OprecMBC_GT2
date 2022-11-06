
bilganjil = int(input("Masukan Range Angka yang di inginkan = "))

def ganjil():
   for i in range(0, bilganjil):
        if i % 2 != 0:

           print(i, end=" ")
            
print("Angka ganjil dari range 0 sampai ", bilganjil)
ganjil()

#ATAU

pilih = int(input("Masukan Pilihan : 1.Ganjil | 2.Genap : "))

if pilih == 1:
    for x in range (12):
        if x % 2 == 1:
            print(x)
else:
    for x in range (12):
        if x % 2 == 0:
            print(x)