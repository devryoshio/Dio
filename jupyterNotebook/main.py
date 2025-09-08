import tensorflow as tf
from pathlib import Path
from PIL import Image
import numpy as np

# Configurações
IMG_SIZE = 224  # tamanho das imagens
BATCH_SIZE = 32
DATASET_DIR = "dataset"

# Função para verificar imagens válidas
def verify_images(path):
    valid_files = []
    for img_path in Path(path).rglob("*.[jp][pn]g"):  # jpg ou png
        try:
            Image.open(img_path).verify()
            valid_files.append(str(img_path))
        except:
            print(f"Imagem corrompida ignorada: {img_path}")
    return valid_files

# Lista de arquivos válidos
all_files = verify_images(DATASET_DIR)

# Dividir em treino e validação
np.random.shuffle(all_files)
split_index = int(len(all_files) * 0.8)
train_files = all_files[:split_index]
val_files = all_files[split_index:]

# Função para carregar e processar imagens
def load_and_preprocess(path):
    # Carregar a imagem
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [IMG_SIZE, IMG_SIZE])
    image = image / 255.0  # normaliza entre 0 e 1

    # Criar o label usando tf.strings
    path = tf.strings.regex_replace(path, "\\\\", "/")  # substitui '\' por '/'
    label = tf.cond(tf.strings.regex_full_match(path, ".*dog.*"), lambda: 1, lambda: 0)

    return image, label

# Criar datasets
train_ds = tf.data.Dataset.from_tensor_slices(train_files)
train_ds = train_ds.map(load_and_preprocess).shuffle(1000).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

val_ds = tf.data.Dataset.from_tensor_slices(val_files)
val_ds = val_ds.map(load_and_preprocess).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

print(f"Treino: {len(train_files)} imagens")
print(f"Validação: {len(val_files)} imagens")
