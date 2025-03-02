from fastapi import APIRouter
from src.models.uncertainties import Uncertainties
from src.controllers.uncertainties_controller import calculate_uncertainties

router = APIRouter()

@router.post("/uncertainties")
def uncertainties(values: Uncertainties):
    return calculate_uncertainties(values.measures, values.uncertaintiesB)
