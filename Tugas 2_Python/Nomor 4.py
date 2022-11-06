#membuat pola n x n dari * dan #
n = int(input("Masukkan n :"))
baris = n
kolom = n
print("Pola N x N")
for i in range(1, baris+1):
    for j in range(1, kolom+1):
        if(i == 1 or i == baris or j == 1 or j == kolom):
            print("*", end = '')
        else:
            print("#", end = '')
    print()
