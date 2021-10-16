# Exercises Service

[![.github/workflows/pipeline.yml](https://github.com/Team-Lisa/python-service/actions/workflows/pipeline.yml/badge.svg?branch=master)](https://github.com/Team-Lisa/python-service/actions/workflows/pipeline.yml)
[![Coverage Status](https://coveralls.io/repos/github/Team-Lisa/exercises-service/badge.svg?branch=master)](https://coveralls.io/github/Team-Lisa/exercises-service?branch=master)

## Env
* Production: https://exercises-service-idioma-play.herokuapp.com/

## Local Mode

#### Requirements

- Python 3.9
- [Poetry](https://python-poetry.org/docs/#installation)

#### Setup
1. run ```poetry install``` 
2. run ```poetry shell``` (create a venv)

#### Running locally
- ```uvicorn api.main:app```

## Using Docker

#### Requirements
- Docker

#### Running locally

1. ```make build``` 
2. ```make start```


## Documentation
You can see the automatic interactive API documentation using the endpoint: ```/docs```

