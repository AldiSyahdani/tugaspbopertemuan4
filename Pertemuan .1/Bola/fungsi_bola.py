import tkinter as tk
from tkinter import messagebox
from bola import hitung_volume_bola, hitung_luas_permukaan_bola

def hitung_bola():
    try:
        jari_jari = float(jari_jari_entry.get())

        volume = hitung_volume_bola(jari_jari)
        luas_permukaan = hitung_luas_permukaan_bola(jari_jari)

        hasil_volume.set(f"Volume Bola: {volume:.2f}")
        hasil_luas.set(f"Luas Permukaan Bola: {luas_permukaan:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk jari-jari bola.")

def main_bola():
    app = tk.Tk()
    app.title("Kalkulator Bola")

    frame = tk.Frame(app)
    frame.pack(padx=10, pady=10)

    jari_jari_label = tk.Label(frame, text="Jari-jari:")
    jari_jari_label.grid(row=0, column=0)
    jari_jari_entry = tk.Entry(frame)
    jari_jari_entry.grid(row=0, column=1)

    hitung_button = tk.Button(frame, text="Hitung", command=hitung_bola)
    hitung_button.grid(row=1, columnspan=2)

    hasil_volume = tk.StringVar()
    hasil_luas = tk.StringVar()

    hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
    hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

    hasil_volume_label.grid(row=2, columnspan=2)
    hasil_luas_label.grid(row=3, columnspan=2)

    app.mainloop()
