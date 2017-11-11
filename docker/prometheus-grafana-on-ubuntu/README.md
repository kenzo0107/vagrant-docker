# Prometheus2.0 + Node Exporter + Grafana + cAdvisor + Nginx + Adminer by Docker-compose

## Overview

![Imgur](https://i.imgur.com/zFciewX.png)

## Precondition

- Ubuntu 16.04.3 LTS \n \l
- Docker version 17.09.0-ce, build afdb6d4
- docker-compose version 1.12.0, build b31ff33

### Install Middleware

- Prometheus 2.0.0
- Node Exporter 0.15.1
- cAdvisor 0.28.0
- Prometheu Adapter
- PostgreSQL 9.6.3
- Grafana 4.6.1
- Nginx 1.13.6
- Adminer

## Usage

```
$ docker-compose up -d

Name                             Command                            State                             Ports
-------------------------------------------------------------------------------------------------------------------------------------
adapter                           /prometheus-postgresql-ada ...    Up
adminer                           entrypoint.sh docker-php-e ...    Up                                8080/tcp
alertmanager                      /bin/alertmanager -config. ...    Up                                9093/tcp
cadvisor                          /usr/bin/cadvisor -logtost ...    Up                                8080/tcp
grafana                           /run.sh                           Up                                3000/tcp
nginx                             nginx -g daemon off;              Up                                0.0.0.0:18080->18080/tcp,
                                                                                         0.0.0.0:3000->3000/tcp, 80/tcp,
                                                                                         0.0.0.0:8080->8080/tcp,
                                                                                         0.0.0.0:9090->9090/tcp
node-exporter                     /bin/node_exporter                Up                                9100/tcp
pgsql                             docker-entrypoint.sh -csyn ...    Up                                5432/tcp
prometheus                        /bin/prometheus --config.f ...    Up                                9090/tcp
```

## Access !

### Prometheus

* Access [http://(your server ip/domain):9090](http://192.168.35.101:9090).

![Imgur](https://i.imgur.com/rg53Xa1.png)

### Grafana

* Access [http://(your server ip/domain):13000](http://192.168.35.101:13000).
* User Account is in `./grafana/env`.
```
GF_SECURITY_ADMIN_USER=admin-user
GF_SECURITY_ADMIN_PASSWORD=admin-pass
```

![Imgur](https://i.imgur.com/fDXVySw.png)

* Configure Datasource

![Imgur](https://i.imgur.com/8SKvdxJ.png)

Configure datasource and click the button "Add".

Fill in datasource configure form with information below:

|*Item*|*Value*|
|---|---|
|Name|Prometheus|
|Type|Prometheus|
|URL|http://prometheus:9090|
|Access|proxy|

![Imgur](https://i.imgur.com/6Cr4WTn.png)

* import Dashboard.json

upload `DockerDashboard.json`.

![Imgur](https://i.imgur.com/cew58vF.png)

You see graphs !

![Imgur](https://i.imgur.com/IicXL5e.png)


### Adminer

* Access [http://(your server ip/domain):8080](http://192.168.35.101:8080).

![Imgur](https://i.imgur.com/ZDH3zmI.png)

### Adminer

* Access [http://(your server ip/domain):18080](http://192.168.35.101:18080).

![Imgur](https://i.imgur.com/uWT7sDC.png)

Fill in login form with information below:

|*Item*|*Value*|
|---|---|
|Server|pgsql|
|Username|prometheus|
|Password|password|
|Database|postgres|

* You see metrics in PostgreSQL.

PostgreSQL >> pgsql >> postgres >> prometheus >> Select: metrics

![Imgur](https://i.imgur.com/cyPrvqC.png)
