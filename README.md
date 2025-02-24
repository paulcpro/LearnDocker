# Learn Dockerfile

| Plugin | README |
| ------ | ------ |
| DockerInteractif | [https://github.com/paulcpro/LearnDocker/tree/main/DockerInteractif] |
| DockerCompose | [https://github.com/paulcpro/LearnDocker/tree/main/DockerCompose] |
| DockerMake | [https://github.com/paulcpro/LearnDocker/tree/main/DockerMake] |
| DockerWebApp | [https://github.com/paulcpro/LearnDocker/tree/main/DockerWebApp] |
| DockerBasics01 | [https://github.com/paulcpro/LearnDocker/tree/main/DockerBasics01] |
| DockerBasics02 | [https://github.com/paulcpro/LearnDocker/tree/main/DockerBasics02] |

## Program Image
```sh
FROM
RUN
WORKDIR
VOLUME
COPY 
ENTRYPOINT
```
- FROM : Permet de récupérer une image ubuntu dans notre cas sur DockerHub
- RUN : Permet d'installer les différentes dépendances pour l'image ubuntu
- WORKDIR : Permet de créer un répertoire de travail où on y placera notre code
- VOLUME : Partage d'un répertoire entre l'hôte et le conteneur de manière persistante
- COPY : Copie le code depuis l'hôte vers le répertoire de travail
- ENTRYPOINT : Définition du point d'entrée par défaut, ici "bash" pour intéragir avec le conteneur