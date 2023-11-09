import tkinter as tk
import fungsi_kerucut

if __name__ == "__main__":
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

    hitung_button = tk.Button(frame, text="Hitung", command=fungsi_kerucut.hitung_kerucut)
    hitung_button.grid(row=2, columnspan=2)

    hasil_volume = tk.StringVar()
    hasil_luas = tk.StringVar()

    hasil_volume_label = tk.Label(frame, textvariable=hasil_volume)
    hasil_luas_label = tk.Label(frame, textvariable=hasil_luas)

    hasil_volume_label.grid(row=3, columnspan=2)
    hasil_luas_label.grid(row=4, columnspan=2)

    app.mainloop()
