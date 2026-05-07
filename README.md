# Sample Calculator API

A simple REST API calculator built with Python and FastAPI.

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the server

```bash
python main.py
```

The server runs on **http://localhost:8787**.

---

## Endpoints

All endpoints accept `POST` requests with a JSON body `{ "a": <number>, "b": <number> }`.

| Endpoint      | Operation      | Example Request          | Example Response                                          |
|---------------|----------------|--------------------------|-----------------------------------------------------------|
| POST /add      | Addition       | `{"a": 10, "b": 5}`      | `{"a": 10, "b": 5, "operation": "addition", "result": 15.0}` |
| POST /subtract | Subtraction    | `{"a": 10, "b": 5}`      | `{"a": 10, "b": 5, "operation": "subtraction", "result": 5.0}` |
| POST /multiply | Multiplication | `{"a": 10, "b": 5}`      | `{"a": 10, "b": 5, "operation": "multiplication", "result": 50.0}` |
| POST /divide   | Division       | `{"a": 10, "b": 5}`      | `{"a": 10, "b": 5, "operation": "division", "result": 2.0}` |

**Division by zero** returns HTTP 400:
```json
{"detail": "Division by zero is not allowed."}
```

**Non-numeric inputs** are rejected with HTTP 422.

---

## API Docs

- Swagger UI: http://localhost:8787/docs
- ReDoc:       http://localhost:8787/redoc
