#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/square/{a}")
def square(a: int):
    return {"product": a * a}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"product": a * b}

@app.get("/subtract/{a}/{b}")
def subtract(a: int, b: int):
    return {"sum": a - b}
