import tkinter as tk
from tkinter import messagebox
import math

def hitung_volume_bola():
    try:
        jari_jari = float(jari_jari_entry.get())
        volume = (4/3) * math.pi * (jari_jari**3)
        hasil_volume.set(f"Volume Bola: {volume:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk jari-jari bola.")

def hitung_luas_permukaan_bola():
    try:
        jari_jari = float(jari_jari_entry.get())
        luas_permukaan = 4 * math.pi * (jari_jari**2)
        hasil_luas.set(f"Luas Permukaan Bola: {luas_permukaan:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk jari-jari bola.")

app = tk.Tk()
app.title("Kalkulator Bola")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

jari_jari_label = tk.Label(frame, text="Jari-jari:")
jari_jari_label.grid(row=0, column=0)
jari_jari_entry = tk.Entry(frame)
jari_jari_entry.grid(row=0, column=1)

hitung_volume_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_bola)
hitung_volume_button.grid(row=1, column=0)

hitung_luas_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_bola)
hitung_luas_button.grid(row=1, column=1)

hasil_volume = tk.StringVar()
hasil_luas = tk.StringVar()

hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

hasil_volume_label.grid(row=2, columnspan=2)
hasil_luas_label.grid(row=3, columnspan=2)

app.mainloop()