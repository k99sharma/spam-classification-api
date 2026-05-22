import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.prediction import router as prediction_router
from app.core.exception_handler import global_exception_handler

app = FastAPI()

FRONTEND_URL = os.getenv("FRONTEND_URL")

app.include_router(
    prediction_router,
    prefix="/api",
    tags=["Prediction"]
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)