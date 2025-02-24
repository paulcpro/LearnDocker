# Dockerfile Compose

## Commands to use the programmed Image
## Build Image
```sh
docker-compose build
```
- build : Construit les images à partir des services définis dans le .yml

## Instanciate Image
```sh
docker-compose up
```
- up : Démarre les services dans le .yml

## Remove Image
```sh
docker-compose rm -f {service_name}
```
- -f : Permet de supprimer une image ou un conteneur spécifique

