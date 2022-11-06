def main():
    import os
    import time
    print ("="*31)
    print("JADWAL SERAGAM TELKOM UNIVERITY")
    print ("="*31)
    hari = input("Masukkan hari : ")
    if hari == "senin":
        print("Seragam hari senin adalah Kemeja Merah Telkom")
        time.sleep(5)
        os.system('cls')
        main()
    elif hari == "selasa":
        print("Seragam hari selasa adalah Kemeja Putih Telkom")
        time.sleep(5)
        os.system('cls')
        main()
    elif hari == "rabu":
        print("Seragam hari rabu adalah Kemeja putih Telkom")
        time.sleep(5)
        os.system('cls')
        main()
    elif hari == "kamis":
        print("Seragam hari kamis adalah Kemeja kotak-kotak atau kemeja bebas")
        time.sleep(5)
        os.system('cls')
        main()
    elif hari == "jumat":
        print("Seragam hari jumat adalah Kemeja batik atau kemeja bebas")
        time.sleep(5)
        os.system('cls')
        main()
    else:
        print("Data tidak ditemukan, silahkan masukkan lagi")
        time.sleep(3)
        os.system('cls')
        main()
main()