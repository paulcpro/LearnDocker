# Utilisation de l'image de base
FROM ubuntu:20.04

# Installation des dépendances
RUN apt update && apt install -y curl bash

# Ajout du script dans l'image
COPY my_script.sh /usr/local/bin/

# Transformer le fichier en exécutable
RUN chmod +x /usr/local/bin/my_script.sh

# Point d'entrée du conteneur
CMD ["/bin/bash", "-c", "/usr/local/bin/my_script.sh; exec bash"]
