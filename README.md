# Workshop sobre docker

### Instrutor:

- Linkedin ~> [Estevam Rodrigues](https://www.linkedin.com/in/estevamrodrigues/)
- Github ~> [@estevammr](https://github.com/estevammr)

---

## História

- Infra Física
- Virtualização
- Containerização

Containers é semelhante aos **chroot** e **namespace** contidos nos sistemas linux.

## Por que usar?

1. Ambiente semelhantes
2. Aplicação como pacote completo
3. Padronização e replicação
4. Idioma comum entre times
5. Comunidade

## 12 factor apps

"The Twelve-Factor app" (12facor) é um manifesto com uma série de boas práticas para construção de software uitlizando formatos declarativos de automação.

1. **Base de Código**.

> Uma base de código com rastreamento utilizando controle de revisão.

2. **Dependências**
3. **Configurações**
4. **Serviços de Apoio**
5. **Build, release and run**
6. **Processos**
7. **Vínculo de porta**

> Exporte serviços por ligação de porta

8. **Concorrência**

> Dimensione por um modelo de processo

9. **Descartabilidade**

> Maximizar a robustez com inicialização e desligamento rápido

10. **Dev/prod semelhantes**

> Mantenha o desenvolvimento, teste, produção o mais semelhante possível

11. **Logs**

> Trate logs como fluxo de eventos

12. **Processosde Admin**

> Executar tarefas de administração/gerenciamento como processos pontuais

---

## Instalação

Linux:

```bash
$ curl -fsSL https:get.docker.com | bash
```

Mac:

```bash
$ brew cask install docker
```

Windows download:

- https://www.docker.com/products/docker-desktop

#### Comando para testar:

```bash
$ docker container run hello-world
```

---

## Pratica

### Executando um container pt1

- Listar images instaladas no cache da maquina.

```bash
$ docker image list
```

- Baixar image do Nginx na maquina.

```bash
$ docker image pull nginx
```

- Inpecionar a image do ngnix baixada.

```bash
$ docker image inspect nginx
```

### Executando um container pt2

> docker container run \<parâmentro> \<imagem> \<cmd> \<argumento>

**Exemplo**:

```bash
$ docker container run -d --name my-nginx nginx /bin/bash
```

- Rodando o comando docontainer sem ser iterativo(entrar no terminal do container)

```bash
$ docker container run -d --name my-nginx2 nginx
```

- Verificando o container rodando.

```bash
$ docker container ls
```

- Parando todos os containers

```bash
$ docker stop $(docker container ls -aq)
```

### Mapeamento de volumes

- Este é o modelo de comando para mapeamento de volumes da maquina host para dentro do container.

> \$ docker container run -d -v \"\<host>:\<container>" nginx

**Exemplo**

```bash
$ docker container run -d -v "/home/configs/nginx:/etc/nginx/config.d" nginx
```

### Mapeamento de portas

Este é o modelo de comando para mapeamento de volumes da maquina host para dentro do container.

> \$ docker container run -d -p \"\<host>:\<container>" nginx

**Exemplo**:

```bash
$ docker container run -d -p 1234:80 nginx
```

##### docker com orquestardor

```bash
$ docker container run -d -m 1024M -c 512 nginx
```

### Start and Stop Container

> docker container start \<id> or \<name>

> docker container stop \<id> or \<name>

### Modo iterativo no container

> docker container exec -it \<id> or \<name> /bin/bash

---

## Imagens

### Commit

```bash
$ docker container run -it --name my-ubuntu ubuntu:16.04 bash
(docker-shell) $ apt-get update
(docker-shell) $ apt-get install nginx -y
(docker-shell) $ exit
$ docker container commit my-ubuntu
```

### Dockerfile

> Image Base ~> Dockerfile(Modificações na Imagem base) ~> Image

#### Gerar nossa imagem

Com base em Dockerfile exemplo na pasta **Exemplo01**, vamos gerar nossa propria image com o comando abaixo:

```bash
$ cd Exemplo01
$ docker image build -t ubuntaum:nginx_dockerfile .
```

---

## Docker Compose

### Instalação

- Linux

```bash
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

#### Verificando a instalação

```bash
$ docker-compose -v
```

### Executar docker-compose

Entrar na pasta **PythonDocker** e executar o comando a baixo:

```bash
$ docker-compose up -d
```
