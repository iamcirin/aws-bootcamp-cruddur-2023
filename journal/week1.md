# Week 1 — App Containerization

## Run the app with docker-compose.yml file.png
remarque: the port on .env.example (backend-flask folder) was set to 3001 so I had to change it for the app to work

![run-the-app-with-docker-compose-file.png](assets/week1/run-the-app-with-docker-compose-file.png)


## Run the dockerfile CMD as an external script

![](assets/week1/Run-the-dockerfile-CMD-as-an-external-script.png)


## Push and tag a image to DockerHub (they have a free tier)
  - I pulled an ubuntu image from docker hub
  - ran a container from the image
  - installed git to customize it
  - committed the container to an image
  - tagged and pushed the image

![](assets/week1/tag-Docker-image.png)


![](assets/week1/push-docker-image.png)

## Use multi-stage building for a Dockerfile build

![](assets/week1/multi-stage-building.png)



## Implement a healthcheck in the V3 Docker compose file

![](assets/week1/healthcheck.png)


## install Docker on your localmachine and get the same containers running outside of Gitpod / Codespaces

![](assets/week1/install-docker-locally.png)

  - pushed the images from gitpod to docker hub
  - pulled the images to my local machine
  - ran the images locally

![](assets/week1/run-containers-locally.png)
