import tkinter as tk
from tkinter import messagebox
from limas_segitiga import hitung_volume_limas_segitiga, hitung_luas_permukaan_limas_segitiga

def hitung_limas_segitiga():
    try:
        panjang_alas = float(panjang_alas_entry.get())
        tinggi = float(tinggi_entry.get())
        sisi_miring = float(sisi_miring_entry.get())

        volume = hitung_volume_limas_segitiga(panjang_alas, tinggi)
        luas_permukaan = hitung_luas_permukaan_limas_segitiga(panjang_alas, tinggi, sisi_miring)

        hasil_volume.set(f"Volume Limas Segitiga: {volume:.2f}")
        hasil_luas.set(f"Luas Permukaan Limas Segitiga: {luas_permukaan:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk panjang alas, tinggi, dan sisi miring limas segitiga.")

def main_limas_segitiga():
    app = tk.Tk()
    app.title("Kalkulator Limas Segitiga")

    frame = tk.Frame(app)
    frame.pack(padx=10, pady=10)

    panjang_alas_label = tk.Label(frame, text="Panjang Alas:")
    panjang_alas_label.grid(row=0, column=0)
    panjang_alas_entry = tk.Entry(frame)
    panjang_alas_entry.grid(row=0, column=1)

    tinggi_label = tk.Label(frame, text="Tinggi:")
    tinggi_label.grid(row=1, column=0)
    tinggi_entry = tk.Entry(frame)
    tinggi_entry.grid(row=1, column=1)

    sisi_miring_label = tk.Label(frame, text="Sisi Miring:")
    sisi_miring_label.grid(row=2, column=0)
    sisi_miring_entry = tk.Entry(frame)
    sisi_miring_entry.grid(row=2, column=1)

    hitung_button = tk.Button(frame, text="Hitung", command=hitung_limas_segitiga)
    hitung_button.grid(row=3, columnspan=2)

    hasil_volume = tk.StringVar()
    hasil_luas = tk.StringVar()

    hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
    hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

    hasil_volume_label.grid(row=4, columnspan=2)
    hasil_luas_label.grid(row=5, columnspan=2)

    app.mainloop()
