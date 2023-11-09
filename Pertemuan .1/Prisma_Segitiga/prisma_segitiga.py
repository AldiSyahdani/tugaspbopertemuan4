def hitung_volume_prisma_segitiga(panjang_alas, tinggi, tinggi_prisma):
    """Menghitung volume prisma segitiga."""
    volume = 0.5 * panjang_alas * tinggi * tinggi_prisma
    return volume

def hitung_luas_permukaan_prisma_segitiga(panjang_alas, tinggi, tinggi_prisma):
    """Menghitung luas permukaan prisma segitiga."""
    luas_permukaan = panjang_alas * tinggi + 3 * (0.5 * panjang_alas * tinggi_prisma)
    return luas_permukaan
