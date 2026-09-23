"""Numerical Analysis API using FastAPI and NumPy."""

import numpy as np
from fastapi import FastAPI, Path


app = FastAPI(
    title="NumPy Calculation API",
    description="GET APIs for numerical analysis using NumPy.",
    version="1.0.0",
)

NUMBERS = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])


def scalar_stats():
    """Calculate the requested statistics from the shared NumPy array."""
    return {
        "mean": float(np.mean(NUMBERS)),
        "median": float(np.median(NUMBERS)),
        "standard_deviation": float(np.std(NUMBERS)),
        "variance": float(np.var(NUMBERS)),
        "maximum": int(np.max(NUMBERS)),
        "minimum": int(np.min(NUMBERS)),
    }


@app.get("/numbers")
def get_numbers():
    return {"numbers": NUMBERS.tolist()}


@app.get("/mean")
def get_mean():
    return {"mean": float(np.mean(NUMBERS))}


@app.get("/median")
def get_median():
    return {"median": float(np.median(NUMBERS))}


@app.get("/std")
def get_standard_deviation():
    return {"standard_deviation": float(np.std(NUMBERS))}


@app.get("/variance")
def get_variance():
    return {"variance": float(np.var(NUMBERS))}


@app.get("/maximum")
def get_maximum():
    return {"maximum": int(np.max(NUMBERS))}


@app.get("/minimum")
def get_minimum():
    return {"minimum": int(np.min(NUMBERS))}


@app.get("/sum")
def get_sum():
    return {"sum": int(np.sum(NUMBERS))}


@app.get("/even")
def get_even_numbers():
    return {"even": NUMBERS[NUMBERS % 2 == 0].tolist()}


@app.get("/odd")
def get_odd_numbers():
    return {"odd": NUMBERS[NUMBERS % 2 != 0].tolist()}


@app.get("/stats")
def get_stats():
    return scalar_stats()


@app.get("/table/{number}")
def get_multiplication_table(
    number: int = Path(..., description="The number whose multiplication table is required.", ge=1),
):
    multipliers = np.arange(1, 11)
    products = number * multipliers
    return {
        "number": number,
        "table": [
            {"multiplier": int(multiplier), "result": int(result)}
            for multiplier, result in zip(multipliers, products)
        ],
    }
