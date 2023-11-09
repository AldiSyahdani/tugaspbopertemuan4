import tkinter as tk
from tkinter import messagebox
from tabung import hitung_volume_tabung, hitung_luas_permukaan_tabung

def hitung_tabung():
    try:
        jari_jari = float(jari_jari_entry.get())
        tinggi = float(tinggi_entry.get())

        volume = hitung_volume_tabung(jari_jari, tinggi)
        luas_permukaan = hitung_luas_permukaan_tabung(jari_jari, tinggi)

        hasil_volume.set(f"Volume Tabung: {volume:.2f}")
        hasil_luas.set(f"Luas Permukaan Tabung: {luas_permukaan:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk jari-jari dan tinggi tabung.")

app = tk.Tk()
app.title("Kalkulator Tabung")

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

hitung_button = tk.Button(frame, text="Hitung", command=hitung_tabung)
hitung_button.grid(row=2, columnspan=2)

hasil_volume = tk.StringVar()
hasil_luas = tk.StringVar()

hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

hasil_volume_label.grid(row=3, columnspan=2)
hasil_luas_label.grid(row=4, columnspan=2)

app.mainloop()