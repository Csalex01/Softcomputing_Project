# Building the Docker image

```
docker build --tag [ Desired Tag Name ] .
```

# Running the Docker container

```
docker run -it -v ./data:/data [ Existing Image Name ]
```

# Enable the virtual environment

Inside the docker container type the following:
```
source /env/bin/activate
```