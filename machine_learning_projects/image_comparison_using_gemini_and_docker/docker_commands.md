once the dockerfile is setup, run the following command to create an image

## Build Image
docker build -t my-flask-app:latest .
  •	docker build – Build an image
	•	-t my-flask-app:latest – Tag/name the image (name:tag)
	•	. – Build context (current folder; all files here can be copied into image)

Once the image is built, run the following to start the container

## List images
docker images

## Run Image
docker run --name my-flask-container -p 5000:5000 my-flask-app:latest
  •	docker run – Start a container from an image
	•	--name my-flask-container – Optional, gives the container a friendly name
	•	-p 5000:5000 – Map host port 5000 → container port 5000
	•	Format: HOST_PORT:CONTAINER_PORT
	•	my-flask-app:latest – Image name

Now open your browser and go to:
## http://localhost:5000 
→ you should see "Hello from Docker!"

## To Stop container
docker stop my-flask-container

## To start the container again
docker start my-flask-container

## To see running containers
docker ps

## To see all containers
docker ps -a
