# backend.py

from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Charger le modèle
model = load_model("PFA3.h5", compile=False)

def preprocess(img):
    try:
        # Redimensionner l'image à la taille attendue par le modèle
        img = img.resize((224, 224))
        # Convertir l'image en tableau NumPy
        img_array = np.asarray(img)
        # Vérifier si l'image est en niveaux de gris
        if len(img_array.shape) == 2:  # Si l'image a seulement 2 dimensions, elle est en niveaux de gris
            # Convertir l'image en RGB en dupliquant les canaux
            img_array = np.stack((img_array,) * 3, axis=-1)
        # S'assurer que l'image a trois canaux de couleur (RGB)
        if img_array.shape[2] != 3:
            raise ValueError("L'image n'a pas trois canaux de couleur (RGB)")
        # Normaliser les valeurs des pixels de l'image entre 0 et 1
        img_array = img_array.astype('float32') / 255.0
        # Ajouter une dimension de lot
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        raise ValueError("Erreur lors du prétraitement de l'image: " + str(e))


def predict_avc(uploaded_file):
    try:
        # Lire l'image téléchargée
        img = Image.open(uploaded_file)
        # Prétraiter l'image
        img_processed = preprocess(img)

        # Effectuer la prédiction
        pred = model.predict(img_processed)
        rec = pred[0][0]

        return rec
    except Exception as e:
        raise ValueError("Erreur lors de la prédiction: " + str(e))
