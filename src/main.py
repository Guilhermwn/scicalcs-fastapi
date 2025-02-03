from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

import statistics
import math


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Uncertainties(BaseModel):
    measures: str

def get_number_list(numbers:str):
    num_pattern = re.compile(r'[+-]?(?:\d+\.\d+|\d+\.\d*|\.\d+|\d+)')
    finder = re.findall(num_pattern, numbers)
    return list(map(float, finder))


@app.post("/uncertainties")
def uncertainties(measures: Uncertainties):
    measures_list = get_number_list(measures.measures)
    _size = len(measures_list)

    _mean = statistics.mean(measures_list)
    _std_dev = statistics.stdev(measures_list)
    _uncertainty_a = math.sqrt(_std_dev / _size)

    return {
        "mean": _mean,
        "stdDev": _std_dev,
        "uncertaintyA": _uncertainty_a
    } 

