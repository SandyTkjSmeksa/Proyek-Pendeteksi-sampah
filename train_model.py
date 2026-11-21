
import tensorflow as tf
from tensorflow.keras import layers, models

# Ukuran gambar
IMG_SIZE = (160, 160)
BATCH_SIZE = 2

# Mengambil gambar dari folder dataset
train_data = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="binary",
    shuffle=True
)

print("Dataset berhasil dibaca!")
print("Nama kelas:", train_data.class_names)
# Mengambil model AI MobileNetV2
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(160, 160, 3),
    include_top=False,
    weights="imagenet"
)

# Membekukan model dasar
base_model.trainable = False

print("Model MobileNetV2 berhasil dimuat!")
# Membuat model klasifikasi
model = models.Sequential([
    layers.Input(shape=(160, 160, 3)),
    layers.Rescaling(1./127.5, offset=-1),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1, activation="sigmoid")
])

# Mengatur proses pembelajaran
# Mengatur proses pembelajaran
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("Model berhasil dibuat!")
# Melatih model AI
print("Mulai melatih model...")

    
model.fit(
    train_data,
    epochs=5
)

# Menyimpan model
model.save("sampah_model.keras")

print("Model berhasil dilatih dan disimpan!")