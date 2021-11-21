#!/bin/bash
docker tag lightsail-hello-world jeremysimmons/lightsail-hello-world
docker login
docker push jeremysimmons/lightsail-hello-world
