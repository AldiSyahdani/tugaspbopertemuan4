# Modul balok
def hitung_volume(panjang, lebar, tinggi):
    """Menghitung volume balok."""
    volume = panjang * lebar * tinggi
    return volume

def hitung_luas_permukaan(panjang, lebar, tinggi):
    """Menghitung luas permukaan balok."""
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return luas_permukaan

# Fungsi utama kalkulator
def kalkulator_balok():
    print("Selamat datang di Kalkulator Balok")
    
    while True:
        print("\nPilihan Menu:")
        print("1. Hitung Volume")
        print("2. Hitung Luas Permukaan")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            volume = hitung_volume(panjang, lebar, tinggi)
            print("Volume balok adalah:", volume)
        
        elif pilihan == '2':
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            luas_permukaan = hitung_luas_permukaan(panjang, lebar, tinggi)
            print("Luas permukaan balok adalah:", luas_permukaan)
        
        elif pilihan == '3':
            print("Terima kasih telah menggunakan Kalkulator Balok.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    kalkulator_balok()
