# Imagem Base
FROM ubuntu:16.04

# Commando personalizado
RUN apt-get update && apt-get install nginx -y

# Copiando o arquivo texto para dentro do docker
COPY rentcars.txt /tmp/rentcars.txt

# Acessando a imagem pelo comando bash
CMD bash