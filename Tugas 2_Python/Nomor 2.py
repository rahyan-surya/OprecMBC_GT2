print("-" * 40)
print("=== Program Menghitung Total Belanja ===")
print("-" * 40)

x = int(input('Masukkan total belanja: '))
y = input('Apakah Anda Member? (y/t): ')
print("=" * 40)

if(y == 'y'):
    if(x > 1000000):
        print("Selamat Anda mendapatkan diskon 8%")
    elif(500000<=x<=1000000):
        print("Selamat Anda mendapatkan diskon 7%")
    else:
        print("Selamat Anda mendapatkan diskon 5%")
elif(y == 't'):
    if(x > 1000000):
        print("Selamat Anda mendapatkan diskon 3%")
    elif(500000<=x<=1000000):
        print("Selamat Anda mendapatkan diskon 2%")
    else:
        print("Mohon maaf Anda belum mendapatkan diskon")
else:
    print("yang Anda masukkan tidak valid")
