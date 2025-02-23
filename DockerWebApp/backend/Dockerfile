# Utiliser une image Python
FROM python:3.9-slim

# Installer les outils nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire /app si nécessaire et définir comme répertoire de travail
WORKDIR /app

# Copier le fichier de dépendances
COPY requirements.txt /app/requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code de l'application
COPY . /app

# Exposer le port utilisé par Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app.py"]
