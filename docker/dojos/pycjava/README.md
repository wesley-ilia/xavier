  &#xa0;

  <!-- <a href="https://desafio_cezar.netlify.app">Demo</a> -->
</div>

<h1 align="center">Docker Py C Java </h1>

</p>

<p align="center">
  <a href="#about">About</a> &#xa0; | &#xa0;
  <a href="#features">Features</a> &#xa0; | &#xa0;
  <a href="#libraries">Libraries</a> &#xa0; | &#xa0;
  <a href="#requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#starting">Starting</a> &#xa0; | &#xa0;
  <a href="#running">Running</a> &#xa0; | &#xa0;
  <a href="#testing">Testing</a> &#xa0; | &#xa0;
  <a href="#exiting">Exiting</a> &#xa0; | &#xa0;
  <a href="https://github.com/cpereira42" target="_blank">Author</a>
</p>

<br>

## About ##
This project is a game style Jokenpo, but with another options:

The options are:
1 - Py
2 - C
3 - Java

C win to Py, Py win to Java and Jaba win do C. <br>
The application was containerized in an environment with Python 3.9 

## Features ##
In this game, the players choice, his options, 
and after the programa will show the winner.

## Libraries ##

## Requirements ##
Before starting, you need to have [Docker](https://docs.docker.com/get-docker/) installed.

## Starting ##

```bash
# Clone this project
$ git clone https://github.com/wesley-ilia/xavier.git

# Access
$ cd docker

# Create a docker image and run docker
bash run.sh

# Go to the pycjava folder into the container
cd dojos/pycjava


```

## Running ##
```bash
# To start the game
python app/pycjava.py

```

## Testing ##
```bash
# To run some automatic tests
python -m unittest tests/test_pycjava.py
```

## Exiting ##
```bash

# To exit container
exit

# To remove container
docker rm container_labs

# To remove the docker image
docker rmi image_labs
```


&#xa0;

<a href="#top">Back to top</a>
