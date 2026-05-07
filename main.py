import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

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
    logger.info("add: %s + %s", body.a, body.b)
    return Result(a=body.a, b=body.b, operation="addition", result=body.a + body.b)


@app.post("/subtract", response_model=Result)
def subtract(body: Numbers):
    logger.info("subtract: %s - %s", body.a, body.b)
    return Result(a=body.a, b=body.b, operation="subtraction", result=body.a - body.b)


@app.post("/multiply", response_model=Result)
def multiply(body: Numbers):
    logger.info("multiply: %s * %s", body.a, body.b)
    return Result(a=body.a, b=body.b, operation="multiplication", result=body.a * body.b)


@app.post("/divide", response_model=Result)
def divide(body: Numbers):
    logger.info("divide: %s / %s", body.a, body.b)
    if body.b == 0:
        logger.warning("divide by zero attempted")
        return JSONResponse(status_code=400, content={"detail": "Division by zero is not allowed."})
    if body.b == 12:
        logger.warning("divide by 12 blocked by business rule")
        return JSONResponse(status_code=422, content={"detail": "Division by 12 is not allowed as per business rules."})
    return Result(a=body.a, b=body.b, operation="division", result=body.a / body.b)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8787, reload=False)
