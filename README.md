![Cover Image](cover.png)

# MovieSuggestionMs
This is a movie suggestion microservice.

This service aims to present movies to users based on how they inform they are feeling at the moment,
so it maps the current mood to related movie genres, and randomly returns a suggested movie.

The suggestions are based on the user's input mood and takes into consideration psycology studies that suggests certain 
stimuli help a person get over a bad moment according to how the brain reacts to certain situations.

This project was built using python language at version 3.13.0 and fastAPI framework along with sqlAlchemy, and it
applies DDD pattern. 
Further updates are on the way to turn this into a microservice and will implement RabbitMQ, prior to its deployment in
the near future.

The service will later be integrated into TCF as an addon service to the platform, and it uses their movie database
data to perform the queries.

------------------------------------------------------------------------------------------------------------------------

# How To use:
1 - choose a mood from the list below: 

* sad
* excited
* romantic
* happy
* bored
* angry
* relaxed
* nostalgic
* scared
* adventurous

2 - make a get request to http://127.0.0.1:8000/api/v1/movies/random/{mood} using postman / insomnia / brownser and
substitute "{mood}" with one of the listed
above.

3 - you will receive a response, if successfull, like:
{
    "nota": 7.72,
    "id": 9116,
    "quantidade_de_votos": 3114,
    "ano_lancamento": 1965,
    "genres": "Drama, Família, Musical",
    "titulo_portugues": "A Noviça Rebelde"
}
------------------------------------------------------------------------------------------------------------------------

Alternatively upon running the project you can also check the swagger documentation on: http://127.0.0.1:8000/docs where
you are also able to test the request.

**Observation:** The real database has been removed from the project as a security measurement and also to comply to nda
clauses. If you wish to test the project you can download docker and run the following commands to create a testing
database.

first of all, you must create a .env file in the root of the project and add the variables:
````
DB_HOST=localhost
DB_PORT=3308
DB_DATABASE=mss_test
DB_USERNAME=root
DB_PASSWORD=root
ENVIRONMENT=development
````

open your terminal / bash in the folder where you cloned the project and run the following commands:
```
docker run --name mss-container -e MYSQL_ROOT_PASSWORD=root -p 3308:3306 -v mss-data:/var/lib/mysql -d mysql:8
```

now, activate the venv, if you are on windows run:
````
.venv\Scripts\activate

````
for macOS/Linux:
````
source .venv/bin/activate

````

run the migration script for creating the database in your venv cmd/bash
```
python -m src.movies.infrastructure.scripts.run_migrations_and_seeding
```
run 
````
python -m src.main

````
now you should be able to test the service following steps 1, 2, 3

