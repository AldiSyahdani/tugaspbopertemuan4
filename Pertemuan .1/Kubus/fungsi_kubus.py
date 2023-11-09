def hitung_volume_kubus(sisi):
    """Menghitung volume kubus."""
    return sisi ** 3

def hitung_luas_permukaan_kubus(sisi):
    """Menghitung luas permukaan kubus."""
    return 6 * (sisi ** 2)

def main():
    print("Selamat datang di Kalkulator Kubus")
    
    while True:
        print("\nPilihan Menu:")
        print("1. Hitung Volume")
        print("2. Hitung Luas Permukaan")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            sisi = float(input("Masukkan panjang sisi kubus: "))
            volume = hitung_volume_kubus(sisi)
            print(f"Volume kubus adalah: {volume}")
        
        elif pilihan == '2':
            sisi = float(input("Masukkan panjang sisi kubus: "))
            luas_permukaan = hitung_luas_permukaan_kubus(sisi)
            print(f"Luas permukaan kubus adalah: {luas_permukaan}")
        
        elif pilihan == '3':
            print("Terima kasih telah menggunakan Kalkulator Kubus.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
