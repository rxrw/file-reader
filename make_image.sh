#!/bin/bash
docker build -t file-reader .

docker-compose down --remove-orphans && docker-compose up -d