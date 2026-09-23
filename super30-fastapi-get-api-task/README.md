# Fast GET API Fundamentals

## Objective

This project demonstrates how to create a FastAPI application with static routes, dynamic path parameters, calculations, and JSON responses.

## Installation

From this project directory, install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

```bash
uvicorn main:app --reload
```

The API is available at http://127.0.0.1:8000.

Interactive documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Available GET endpoints

| Endpoint | Example |
| --- | --- |
| `GET /` | `/` |
| `GET /student` | `/student` |
| `GET /course` | `/course` |
| `GET /skills` | `/skills` |
| `GET /add/{num1}/{num2}` | `/add/50/25` |
| `GET /multiply/{num1}/{num2}` | `/multiply/5/8` |
| `GET /square/{number}` | `/square/9` |
| `GET /check/{number}` | `/check/17` |
| `GET /age/{age}` | `/age/25` |
| `GET /table/{number}` | `/table/7` |
| `GET /profile/{name}/{age}` | `/profile/Sudhanshu/37` |
| `GET /number/{number}` | `/number/25` |

All endpoints return JSON. Only GET APIs are implemented.

## Testing examples

```bash
curl http://127.0.0.1:8000/add/50/25
curl http://127.0.0.1:8000/check/20
curl http://127.0.0.1:8000/table/7
```

## Submission

- GitHub repository: `super30-fastapi-get-api-task`
- Author/student: Sudhanshu
- YouTube demonstration: add the published video link here
