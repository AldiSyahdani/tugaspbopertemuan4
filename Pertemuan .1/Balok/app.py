import tkinter as tk
from tkinter import messagebox
from balok import hitung_volume, hitung_luas_permukaan

def hitung():
    try:
        panjang = float(panjang_entry.get())
        lebar = float(lebar_entry.get())
        tinggi = float(tinggi_entry.get())
        
        volume = hitung_volume(panjang, lebar, tinggi)
        luas_permukaan = hitung_luas_permukaan(panjang, lebar, tinggi)
        
        hasil_label.config(text=f"Volume: {volume}\nLuas Permukaan: {luas_permukaan}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk panjang, lebar, dan tinggi.")

app = tk.Tk()
app.title("Kalkulator Balok")

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

hitung_button = tk.Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, columnspan=2)

hasil_label = tk.Label(frame, text="")
hasil_label.grid(row=4, columnspan=2)

app.mainloop()
