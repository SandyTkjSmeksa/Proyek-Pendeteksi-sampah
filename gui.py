
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import tensorflow as tf
import numpy as np
# Memuat model AI
model = tf.keras.models.load_model("sampah_model.keras")

print("Model AI berhasil dimuat!")
# Fungsi untuk memprediksi jenis sampah
def prediksi_sampah(path_gambar):
    gambar = Image.open(path_gambar).convert("RGB")
    gambar = gambar.resize((160, 160))

    gambar_array = np.array(gambar, dtype=np.float32)
    gambar_array = np.expand_dims(gambar_array, axis=0)

    hasil = model.predict(gambar_array, verbose=0)[0][0]

    if hasil >= 0.5:
        jenis_sampah = "ORGANIK"
        keyakinan = hasil * 100
    else:
        jenis_sampah = "ANORGANIK"
        keyakinan = (1 - hasil) * 100

    return jenis_sampah, keyakinan

# Pengaturan tampilan
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Membuat jendela utama
app = ctk.CTk()
app.title("Deteksi Sampah AI")
app.geometry("800x700")
app.resizable(True, True)

# Judul aplikasi
judul = ctk.CTkLabel(
    app,
    text="APLIKASI DETEKSI SAMPAH",
    font=("Arial", 25, "bold")
)
judul.pack(pady=25)

# Keterangan
keterangan = ctk.CTkLabel(
    app,
    text="Deteksi Sampah Organik dan Anorganik Menggunakan AI",
    font=("Arial", 14)
)
keterangan.pack(pady=5)
# Identitas pembuat
identitas = ctk.CTkLabel(
    app,
    text="Dibuat oleh: Sandy | Kelas XI TKJ 1\nSMKN 1 Kediri",
    font=("Arial", 14),
    text_color="gray"
)
identitas.pack(pady=10)

# Tempat menampilkan foto
label_gambar = ctk.CTkLabel(
    app,
    text="Belum ada gambar dipilih",
    width=300,
    height=220,
    fg_color="#eeeeee",
    corner_radius=10
)
label_gambar.pack(pady=20)

# Fungsi memilih foto
def pilih_gambar():
    file = filedialog.askopenfilename(
        title="Pilih Foto Sampah",
        filetypes=[
            ("File Gambar", "*.png *.jpg *.jpeg")
        ]
    )

    if file:
        gambar = Image.open(file)
        gambar.thumbnail((300, 220))

        foto = ctk.CTkImage(
            light_image=gambar,
            dark_image=gambar,
            size=gambar.size
        )

        label_gambar.configure(
            image=foto,
            text=""
        )

        label_gambar.image = foto

        # Melakukan prediksi menggunakan AI
    jenis_sampah, keyakinan = prediksi_sampah(file)

    # Menampilkan hasil deteksi
    hasil.configure(
        text=f"Hasil Deteksi: {jenis_sampah}\nKeyakinan: {keyakinan:.2f}%"
    )

    if jenis_sampah == "ORGANIK":
        keterangan.configure(
            text="Sampah organik berasal dari makhluk hidup dan dapat terurai secara alami."
        )
    else:
        keterangan.configure(
            text="Sampah anorganik sulit terurai secara alami. Contoh: plastik, kaleng, dan kaca."
        )


# Tombol memilih foto
tombol_pilih = ctk.CTkButton(
    app,
    text="PILIH FOTO",
    command=pilih_gambar,
    width=200,
    height=40
)
tombol_pilih.pack(pady=10)

# Hasil deteksi sementara
hasil = ctk.CTkLabel(
    app,
    text="Hasil deteksi akan muncul di sini",
    font=("Arial", 16, "bold")
)
hasil.pack(pady=15)
keterangan = ctk.CTkLabel(
    app,
    text="Keterangan hasil deteksi akan muncul di sini",
    font=("Arial", 13),
    wraplength=400
)
keterangan.pack(pady=5)
# Fungsi menghapus foto
def hapus_gambar():
    label_gambar.configure(
        image=None,
        text="Belum ada gambar dipilih"
    )

    label_gambar.image = None

    hasil.configure(
        text="Hasil deteksi akan muncul di sini"
    )


# Tombol hapus foto
tombol_hapus = ctk.CTkButton(
    app,
    text="HAPUS FOTO",
    command=hapus_gambar,
    width=200,
    height=40,
    fg_color="red",
    hover_color="darkred"
)
tombol_hapus.pack(pady=10)
# Menjalankan aplikasi
app.mainloop()
