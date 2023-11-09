import math

def hitung_volume_kerucut(jari_jari, tinggi):
    """Menghitung volume kerucut."""
    volume = (1/3) * math.pi * (jari_jari**2) * tinggi
    return volume

def hitung_luas_permukaan_kerucut(jari_jari, garis_pelukis):
    """Menghitung luas permukaan kerucut."""
    luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)
    return luas_permukaan
