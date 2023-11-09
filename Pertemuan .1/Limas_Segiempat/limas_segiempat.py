#rumus limas segiempat

def hitung_volume_limas_segiempat(panjang, lebar, tinggi):
    """Menghitung volume limas segiempat."""
    volume = (panjang * lebar * tinggi) / 3
    return volume

def hitung_luas_permukaan_limas_segiempat(panjang, lebar, tinggi):
    """Menghitung luas permukaan limas segiempat."""
    luas_permukaan = panjang * lebar + 2 * (lebar * tinggi + panjang * tinggi)
    return luas_permukaan
