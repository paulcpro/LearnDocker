# Dockerfile Interactive

## Commands to use the programmed Image
## Build Image
```sh
docker build -f Dockerfile.dev -t mon_projet_dev .
```
- -f : Permet de sélectionner un nom précis de Dockerfile
- -t : Permet de donner un nom à l'image
- . : Permet de spécifier le répertoire courant comme contexte de construction

## Run Container made from our Image
```sh
docker run --rm -v $(pwd)/mon_projet_cplusplus:/app mon_projet_dev
```
- --rm : Supprime le conteneur après son arrêt
- -v : Permet de monter un volume entre le conteneur et l'hôte
- $(pwd)/mon_projet_cplusplus : Chemin absolu du répertoire à monter en local
- /app : Chemin du répertoire de travail dans le conteneur
- mon_projet_dev : Nom de l'image à exécuter
