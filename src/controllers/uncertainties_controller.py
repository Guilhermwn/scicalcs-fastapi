import re
import statistics
import math

def get_number_list(numbers:str):
    num_pattern = re.compile(r'[+-]?(?:\d+\.\d+|\d+\.\d*|\.\d+|\d+)')
    finder = re.findall(num_pattern, numbers)
    return list(map(float, finder))

def calculate_uncertainties(measures: str, uncertainties_b):
    measures_list = get_number_list(measures)
    _size = len(measures_list)
    uncertainty_b = get_number_list(uncertainties_b)[0] if uncertainties_b else 0.0

    if _size < 2:
        return {"error": "At least two measurements are required"}

    _mean = statistics.mean(measures_list)
    _std_dev = statistics.stdev(measures_list)
    _uncertainty_a = math.sqrt(_std_dev / _size)
    _uncertainty_b = uncertainty_b
    _uncertainty_c = math.sqrt( _uncertainty_a**2 +  _uncertainty_b**2 )

    return {
        "mean": _mean,
        "stdDev": _std_dev,
        "uncertaintyA": _uncertainty_a,
        "uncertaintyB": _uncertainty_b,
        "uncertaintyC": _uncertainty_c
    }