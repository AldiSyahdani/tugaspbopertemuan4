import tkinter as tk
from tkinter import messagebox
from kerucut import hitung_volume_kerucut, hitung_luas_permukaan_kerucut

def hitung_kerucut():
    try:
        jari_jari = float(jari_jari_entry.get())
        tinggi = float(tinggi_entry.get())

        volume = hitung_volume_kerucut(jari_jari, tinggi)
        luas_permukaan = hitung_luas_permukaan_kerucut(jari_jari, math.sqrt(jari_jari**2 + tinggi**2))

        hasil_volume.set(f"Volume Kerucut: {volume:.2f}")
        hasil_luas.set(f"Luas Permukaan Kerucut: {luas_permukaan:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk jari-jari dan tinggi kerucut.")

def main_kerucut():
    app = tk.Tk()
    app.title("Kalkulator Kerucut")

    frame = tk.Frame(app)
    frame.pack(padx=10, pady=10)

    jari_jari_label = tk.Label(frame, text="Jari-Jari:")
    jari_jari_label.grid(row=0, column=0)
    jari_jari_entry = tk.Entry(frame)
    jari_jari_entry.grid(row=0, column=1)

    tinggi_label = tk.Label(frame, text="Tinggi:")
    tinggi_label.grid(row=1, column=0)
    tinggi_entry = tk.Entry(frame)
    tinggi_entry.grid(row=1, column=1)

    hitung_button = tk.Button(frame, text="Hitung", command=hitung_kerucut)
    hitung_button.grid(row=2, columnspan=2)

    hasil_volume = tk.StringVar()
    hasil_luas = tk.StringVar()

    hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
    hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

    hasil_volume_label.grid(row=3, columnspan=2)
    hasil_luas_label.grid(row=4, columnspan=2)

    app.mainloop()