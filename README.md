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

# Running MMDetection tests

```
python demo/image_demo.py demo/demo.jpg rtmdet_tiny_8xb32-300e_coco.py --weights rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth --device cpu --out-dir /data/outputs
```