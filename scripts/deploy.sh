#!/bin/bash
ssh manager << EOF
docker pull georgerhodes/service-1:latest
docker pull georgerhodes/service-1:latest
docker pull georgerhodes/service-1:latest
docker pull georgerhodes/service-1:latest
docker pull nginx:alpine
git clone https://github.com/George-Rhodes/wekkk9-project.git
cd wekkk9-project
docker stack deploy --compose-file docker-compose.yaml projectApp
EOF