# Utiliser l'image Python 3.8 comme base
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Exposer le port 8501
EXPOSE 8501

# Commande pour démarrer l'application avec Streamlit
CMD ["streamlit", "run", "app.py"]
