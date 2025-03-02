from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.uncertainties_routes import router as uncertainties_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(uncertainties_router)
