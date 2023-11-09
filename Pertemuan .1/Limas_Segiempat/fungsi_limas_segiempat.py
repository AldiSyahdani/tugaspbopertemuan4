import tkinter as tk
from tkinter import messagebox
from limas_segiempat import hitung_volume_limas_segiempat, hitung_luas_permukaan_limas_segiempat

def hitung_limas_segiempat():
    try:
        panjang = float(panjang_entry.get())
        lebar = float(lebar_entry.get())
        tinggi = float(tinggi_entry.get())

        volume = hitung_volume_limas_segiempat(panjang, lebar, tinggi)
        luas_permukaan = hitung_luas_permukaan_limas_segiempat(panjang, lebar, tinggi)

        hasil_volume.set(f"Volume Limas Segiempat: {volume:.2f}")
        hasil_luas.set(f"Luas Permukaan Limas Segiempat: {luas_permukaan:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk panjang, lebar, dan tinggi limas segiempat.")

def main_limas_segiempat():
    app = tk.Tk()
    app.title("Kalkulator Limas Segiempat")

    frame = tk.Frame(app)
    frame.pack(padx=10, pady=10)

    panjang_label = tk.Label(frame, text="Panjang:")
    panjang_label.grid(row=0, column=0)
    panjang_entry = tk.Entry(frame)
    panjang_entry.grid(row=0, column=1)

    lebar_label = tk.Label(frame, text="Lebar:")
    lebar_label.grid(row=1, column=0)
    lebar_entry = tk.Entry(frame)
    lebar_entry.grid(row=1, column=1)

    tinggi_label = tk.Label(frame, text="Tinggi:")
    tinggi_label.grid(row=2, column=0)
    tinggi_entry = tk.Entry(frame)
    tinggi_entry.grid(row=2, column=1)

    hitung_button = tk.Button(frame, text="Hitung", command=hitung_limas_segiempat)
    hitung_button.grid(row=3, columnspan=2)

    hasil_volume = tk.StringVar()
    hasil_luas = tk.StringVar()

    hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
    hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

    hasil_volume_label.grid(row=4, columnspan=2)
    hasil_luas_label.grid(row=5, columnspan=2)

    app.mainloop()
