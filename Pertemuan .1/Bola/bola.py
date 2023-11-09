import math

def hitung_volume_bola(jari_jari):
    """Menghitung volume bola."""
    volume = (4/3) * math.pi * jari_jari**3
    return volume

def hitung_luas_permukaan_bola(jari_jari):
    """Menghitung luas permukaan bola."""
    luas_permukaan = 4 * math.pi * jari_jari**2
    return luas_permukaan
