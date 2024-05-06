# PokeAPI

Poke-berries statistics API

## Project Structure
```bash
tree "app"
```

```bash
app
├── api
│   ├── application.py
│   ├── controllers
│   │   ├── berries.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── router.py
│   ├── schemas
│   │   ├── berries.py
│   │   └── __init__.py
│   └── services
│       ├── berries.py
│       └── __init__.py
├── core
│   ├── exceptions
│   │   ├── berries.py
│   │   └── __init__.py
│   └── __init__.py
├── __init__.py
├── __main__.py
├── settings.py
└── tests
    ├── fixtures
    │   ├── berries.py
    │   └── __init__.py
    ├── __init__.py
    └── test_berries.py

```

## Environment variables
Set your environment variables to the expected value
```bash
APP_POKE_API=https://pokeapi.co/api/v2
```

## Docker
To start up the project use this command (terminal 1):
```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

## Unit Tests
To run the tests use this command (terminal 2):
```bash
docker-compose -f deploy/docker-compose.yml --project-directory . exec api bash
```
Once in the docker terminal run this command:
```bash
pytest -vv .
```

## Snippets
General snippets are attached:
```bash
export $(grep -v '^#' .env | xargs)
```

```bash
docker stop $(docker ps -a -q)
```
