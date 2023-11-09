def hitung_volume(panjang, lebar, tinggi):
    """Menghitung volume balok."""
    volume = panjang * lebar * tinggi
    return volume

def hitung_luas_permukaan(panjang, lebar, tinggi):
    """Menghitung luas permukaan balok."""
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return luas_permukaan
