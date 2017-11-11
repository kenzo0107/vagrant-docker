#!/bin/sh
docker-compose down
docker system prune -f
/usr/bin/docker volume rm $(docker volume ls -qf dangling=true)
