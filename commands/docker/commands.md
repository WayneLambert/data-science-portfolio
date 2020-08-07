# Docker Commands

## [System Commands](https://docs.docker.com/engine/reference/commandline/system/)

### Check Status of All Images, Containers and Volumes

```sh
docker system df -v
```

### Enter a Bash Session Within the Docker Container

```sh
docker exec -it <container_name> /bin/sh
```

### Check Network Settings

```sh
docker network inspect bridge
```

### Remove All Stopped Containers, Dangling Images, and Unused Networks

```sh
docker system prune
```

### Remove All Stopped Containers, Dangling Images, Unused Networks and <span style="color: red;">Unused Volumes</span>

```sh
docker system prune --volumes
```

## [Container Commands](https://docs.docker.com/engine/reference/commandline/container/)

### Stop All Running Containers

```sh
docker stop $(docker ps -a -q)
```

### Remove a Specific Container

```sh
docker container rm <container-name-or-id>
```

### Remove Stopped Containers

```sh
docker container prune
```

### Remove All Containers

```sh
docker rm -f $(docker ps -a -q)
```

## [Image Commands](https://docs.docker.com/engine/reference/commandline/image/)

### Remove a Specific Image

```sh
docker image rmi <image-name-or-id>
```

### Remove All Images

```sh
docker rmi -f $(docker images -a -q)
```

### Remove Dangling Images

```sh
docker image prune
```

## [Volume Commands](https://docs.docker.com/engine/reference/commandline/volume_prune/)

### Remove a Specific Volume

```sh
docker volume rm <volume-name-or-id>
```

### <span style="color: red;">Remove All Volumes Not Attached to a Running Container</span>

```sh
docker volume prune
```

## Sources

<https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/>
