# Student Management API

A RESTful Student Management API built with Flask and PostgreSQL.

---

## Features

- Create Student
- Read Student
- Update Student
- Delete Student
- PostgreSQL Database
- Docker Support
- Docker Compose
- Environment Variables
- Persistent Storage using Docker Volume

---

## Project Structure

```
app
 ├── repositories
 │      memory_repository.py
 │      postgres_repository.py
 │      repository.py
 ├── services
 ├── routes
 ├── db.py
 ├── models.py
 └── app.py
```

---

## Architecture

This project follows the Repository Pattern.

Initially the project used **MemoryRepository**.

For this assignment only **repository.py** was changed to use **PostgresRepository**.

The Service Layer and Routes were not modified.

This demonstrates separation of concerns and makes storage easily replaceable.

---

## Environment Variables

Create a `.env` file.

```
DB_HOST=db
DB_PORT=5432
DB_NAME=studentdb
DB_USER=postgres
DB_PASSWORD=postgres
```

---

## Run

```bash
docker compose up --build
```

App

```
http://localhost:5000
```

---

## API Endpoints

GET

```
/students
```

GET

```
/students/{id}
```

POST

```
/students
```

PUT

```
/students/{id}
```

DELETE

```
/students/{id}
```

---

## Example JSON

```json
{
  "name": "Karan",
  "age": 21,
  "course": "Computer Science"
}
```

---

## Persistence Test

Steps performed

1. Started the application using

```
docker compose up --build
```

2. Added a student using POST.

3. Verified using GET.

4. Stopped containers

```
docker compose down
```

5. Started again

```
docker compose up
```

6. Retrieved the student again.

Result

The student data was still present.

This confirms Docker Volume persistence.

---

## Technologies

- Flask
- PostgreSQL
- Docker
- Docker Compose
- Python