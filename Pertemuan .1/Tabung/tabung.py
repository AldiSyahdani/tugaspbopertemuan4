import math

def hitung_volume_tabung(jari_jari, tinggi):
    """Menghitung volume tabung."""
    volume = math.pi * (jari_jari**2) * tinggi
    return volume

def hitung_luas_permukaan_tabung(jari_jari, tinggi):
    """Menghitung luas permukaan tabung."""
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return luas_permukaan
