import tkinter as tk
from tkinter import messagebox

def hitung_volume_prisma_segitiga():
    try:
        panjang_alas = float(panjang_alas_entry.get())
        tinggi = float(tinggi_entry.get())
        tinggi_prisma = float(tinggi_prisma_entry.get())

        volume = 0.5 * panjang_alas * tinggi * tinggi_prisma
        hasil_volume.set(f"Volume Prisma Segitiga: {volume:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk panjang alas, tinggi segitiga, dan tinggi prisma segitiga.")

def hitung_luas_permukaan_prisma_segitiga():
    try:
        panjang_alas = float(panjang_alas_entry.get())
        tinggi = float(tinggi_entry.get())
        tinggi_prisma = float(tinggi_prisma_entry.get())

        luas_permukaan = panjang_alas * tinggi + 3 * (0.5 * panjang_alas * tinggi_prisma)
        hasil_luas.set(f"Luas Permukaan Prisma Segitiga: {luas_permukaan:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk panjang alas, tinggi segitiga, dan tinggi prisma segitiga.")

app = tk.Tk()
app.title("Kalkulator Prisma Segitiga")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

panjang_alas_label = tk.Label(frame, text="Panjang Alas Segitiga:")
panjang_alas_label.grid(row=0, column=0)
panjang_alas_entry = tk.Entry(frame)
panjang_alas_entry.grid(row=0, column=1)

tinggi_label = tk.Label(frame, text="Tinggi Segitiga:")
tinggi_label.grid(row=1, column=0)
tinggi_entry = tk.Entry(frame)
tinggi_entry.grid(row=1, column=1)

tinggi_prisma_label = tk.Label(frame, text="Tinggi Prisma Segitiga:")
tinggi_prisma_label.grid(row=2, column=0)
tinggi_prisma_entry = tk.Entry(frame)
tinggi_prisma_entry.grid(row=2, column=1)

hitung_volume_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_prisma_segitiga)
hitung_volume_button.grid(row=3, column=0)

hitung_luas_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_prisma_segitiga)
hitung_luas_button.grid(row=3, column=1)

hasil_volume = tk.StringVar()
hasil_luas = tk.StringVar()

hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

hasil_volume_label.grid(row=4, columnspan=2)
hasil_luas_label.grid(row=5, columnspan=2)

app.mainloop()