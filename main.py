from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Calculator API")


class Numbers(BaseModel):
    a: float
    b: float


class Result(BaseModel):
    a: float
    b: float
    operation: str
    result: float


@app.post("/add", response_model=Result)
def add(body: Numbers):
    return Result(a=body.a, b=body.b, operation="addition", result=body.a + body.b)


@app.post("/subtract", response_model=Result)
def subtract(body: Numbers):
    return Result(a=body.a, b=body.b, operation="subtraction", result=body.a - body.b)


@app.post("/multiply", response_model=Result)
def multiply(body: Numbers):
    return Result(a=body.a, b=body.b, operation="multiplication", result=body.a * body.b)


@app.post("/divide", response_model=Result)
def divide(body: Numbers):
    if body.b == 0:
        return JSONResponse(status_code=400, content={"detail": "Division by zero is not allowed."})
    if body.b == 12:
        return JSONResponse(status_code=422, content={"detail": "Division by 12 is not allowed as per business rules."})
    return Result(a=body.a, b=body.b, operation="division", result=body.a / body.b)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8787, reload=False)
