
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

# Pengaturan tampilan
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# Membuat jendela utama
app = ctk.CTk()
app.title("Deteksi Sampah AI")
app.geometry("700x550")
app.resizable(False, False)

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

# Menjalankan aplikasi
app.mainloop()
