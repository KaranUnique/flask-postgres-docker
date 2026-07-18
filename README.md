# Student Management API

A Flask REST API using PostgreSQL and Docker.

## Run

```bash
docker compose up --build
```

API runs on:

```
http://localhost:5000
```

## Endpoints

GET /students

GET /students/{id}

POST /students

PUT /students/{id}

DELETE /students/{id}

### Example JSON

```json
{
  "name": "Karan",
  "age": 21,
  "course": "Computer Science"
}
```

Persistence Test

1. Started the application using:

   docker compose up

2. Added a student using POST /students

3. Stopped everything:

   docker compose down

4. Started again:

   docker compose up

5. Called GET /students

6. Verified the student record was still present because PostgreSQL data is stored in a Docker volume.