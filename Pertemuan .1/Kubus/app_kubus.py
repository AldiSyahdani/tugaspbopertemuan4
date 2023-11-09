import tkinter as tk
from tkinter import messagebox

def hitung_volume_kubus():
    try:
        sisi = float(sisi_entry.get())
        volume = sisi ** 3
        hasil_volume.set(f"Volume Kubus: {volume}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk panjang sisi kubus.")

def hitung_luas_permukaan_kubus():
    try:
        sisi = float(sisi_entry.get())
        luas_permukaan = 6 * (sisi ** 2)
        hasil_luas.set(f"Luas Permukaan Kubus: {luas_permukaan}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk panjang sisi kubus.")

app = tk.Tk()
app.title("Kalkulator Kubus")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

sisi_label = tk.Label(frame, text="Panjang Sisi:")
sisi_label.grid(row=0, column=0)
sisi_entry = tk.Entry(frame)
sisi_entry.grid(row=0, column=1)

hitung_volume_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_kubus)
hitung_volume_button.grid(row=1, column=0)

hitung_luas_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_kubus)
hitung_luas_button.grid(row=1, column=1)

hasil_volume = tk.StringVar()
hasil_luas = tk.StringVar()

hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

hasil_volume_label.grid(row=2, columnspan=2)
hasil_luas_label.grid(row=3, columnspan=2)

app.mainloop()