def hitung_volume_limas_segitiga(panjang_alas, tinggi):
    """Menghitung volume limas segitiga."""
    volume = (1/3) * (panjang_alas**2) * tinggi
    return volume

def hitung_luas_permukaan_limas_segitiga(panjang_alas, tinggi, sisi_miring):
    """Menghitung luas permukaan limas segitiga."""
    luas_permukaan = (panjang_alas**2) + (2 * panjang_alas * sisi_miring)
    return luas_permukaan
