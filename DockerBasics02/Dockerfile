# Utilisation de l'image de base
FROM python:3.9

# Copier le code source
WORKDIR /app
COPY . /app

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Lancer l'application Flask
CMD ["python", "app.py"]
