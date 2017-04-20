## Vagrant + Docker-Compose

## Preference

- Mac OS X 10.12.4
- Vagrant 1.9.3
- VirtualBox 5.1.18r114002
- Ubuntu 14.04.5 LTS
- Docker 17.04.0-ce
- Docker-Compose 1.12.0

## Install Steps

```
macOS%$ git clone https://github.com/kenzo0107/vagrant-docker
macOS%$ cd ./vagrant-docker
macOS%$ vagrant up
macOS%$ vagrant ssh
vagrant%$
```

- Install extra package

```
vagrant%$ sudo apt-get update
vagrant%$ sudo apt-get -y install \
    wget \
    linux-image-extra-$(uname -r) \
    linux-image-extra-virtual
```

- Install docker

```
vagrant%$ wget -qO- https://get.docker.com/ | sh

vagrant%$ docker --version
Docker version 17.04.0-ce, build 4845c56

vagrant%$ sudo usermod -aG docker vagrant
```

- Install docker-compose

```
vagrant%$ curl -L "https://github.com/docker/compose/releases/download/1.12.0/docker-compose-$(uname -s)-$(uname -m)" >  ~/docker-compose

vagrant%$ chmod +x ~/docker-compose
vagrant%$ sudo mv docker-compose /usr/bin/

vagrant%$ docker-compose --version
docker-compose version 1.12.0, build b31ff33
```

-  logout and login again to make usermod enabled.

```
vagrant%$ exit
macOS%$ vagrant ssh
```
