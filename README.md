# PokeAPI

Poke-berries statistics API

## Project Structure
```bash
tree "app"
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
