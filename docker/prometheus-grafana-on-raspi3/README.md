# Prometheus + Node Exporter + Grafana + cAdvisor + Nginx by Docker-compose on Raspberry PI3

## Precondition

- Raspberry Pi 3 Model B (Raspbian GNU/Linux 8)
- Docker version 17.04.0-ce, build 4845c56
- docker-compose version 1.9.0, build 2585387

## install docker

```
raspi%$ wget -qO- https://get.docker.com/ | sh
raspi%$ sudo usermod -aG docker pi
raspi%$ sudo gpasswd -a $USER docker
```

## install docker-compose

```
raspi%$ sudo apt-get update
raspi%$ sudo apt-get install -y apt-transport-https
raspi%$ echo "deb https://packagecloud.io/Hypriot/Schatzkiste/debian/ jessie main" | raspi%sudo tee /etc/apt/sources.list.d/hypriot.list
raspi%$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 37BBEE3F7AD95B3F
raspi%$ sudo apt-get update
raspi%$ sudo apt-get install docker-compose
```

- display version

```
raspi%$ docker-compose --version
docker-compose version 1.9.0, build 2585387
```

## Setting Project

```
raspi%$ cd ~
raspi%$ git clone https://github.com/kenzo0107/vagrant-docker
raspi%$ cd vagrant-docker/docker/prometheus-grafana-on-raspi3

// Nginx
raspi%$ htpasswd -c nginx/conf/conf.d/.htpasswd admin-user
New password: (「admin-pass」と入力しEnter)
Re-type new password: (「admin-pass」と入力しEnter)
Adding password for user admin-user

raspi%$ cat nginx/conf/conf.d/.htpasswd
admin-user:$apr1$JLxC83lt$uO7aEn9Z59fZtba4EA7C6/

raspi%$ docker-compose up -d
```

### Point !

- docker-compose.yml  

The `user:pass(hash)` in .htpasswd must be the same as the environment variable - GF_SECURITY_ADMIN_USER, GF_SECURITY_ADMIN_PASSWORD - specified in this file.

```
    environment:
      GF_SECURITY_ADMIN_USER: admin-user
      GF_SECURITY_ADMIN_PASSWORD: admin-pass
```
